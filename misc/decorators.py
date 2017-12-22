# -*- coding: utf-8 -*-
from django.http import HttpResponse
import struct
import zlib
import time
import xml2json
#from collections import OrderedDict
from django.template import loader
from django.utils.html import escape
from errorcode import ERROR_CODE, ERROR_MESSAGE
from conf import VERSION, BUILD
from datetime import datetime

def timestamp(_datetime=None):
    if (not _datetime) or (not isinstance(_datetime, datetime)):
        _datetime = datetime.now()
    _timestamp = time.mktime(_datetime.timetuple())
    _timestamp = "%.0f" % _timestamp
    return _timestamp


def long_to_bytes(n, blocksize = 0):
    """long_to_bytes(n:long, blocksize:int) : string
    Convert a long integer to a byte string.

    If optional blocksize is given and greater than zero, pad the front of the
    byte string with binary zeros so that the length is a multiple of
    blocksize.
    """
    # after much testing, this algorithm was deemed to be the fastest
    s = ''
    n = long(n)
    pack = struct.pack
    while n > 0:
        s = pack('>I', n & 0xffffffffL) + s
        n = n >> 32
    # strip off leading zeros
    for i in range(len(s)):
        if s[i] != '\000':
            break
    else:
        # only happens when n == 0
        s = '\000'
        i = 0
    s = s[i:]
    # add back some pad bytes.  this could be done more efficiently w.r.t. the
    # de-padding being done above, but sigh...
    if blocksize > 0 and len(s) % blocksize:
        s = (blocksize - len(s) % blocksize) * '\000' + s
    return s

def data_compress( _buffer, level=6 ):
    if (_buffer is None) or (_buffer==""):
        return 0, ""
    _c = zlib.compress(_buffer, level)
    _l = len(_c)
    if _l>=100:
        #swap _h<>_t
        _h = 11
        _t = -51
        _converted = _c[:_h]+_c[_t]+_c[_h+1:_t]+_c[_h]+_c[_t+1:]
    else:
        _converted = _c
    return len(_buffer), _converted

def compress_response(_buffer):
    _length, _compressed = data_compress(_buffer)
    response= HttpResponse(mimetype='application/octet-stream')
    response.write(long_to_bytes(_length,10))
    response.write(_compressed)
    return response

def compile_response(request, _template, _context, _force_compress=False, **_kwargs):
    # Set Custom vary flag:
    request.CUSTOM_VARY = True

    _context.update({"version": "%s - %s" % (VERSION, BUILD)})
    _context.update({"timestamp": timestamp()})

    if ('output' in _kwargs) and (_kwargs['output'] is not None):
        _outfmt = _kwargs['output'].lower()
    else:
        _outfmt = request.REQUEST.get("output", None) or "xml"
        if _outfmt:  _outfmt = _outfmt.lower()
    if _outfmt not in ["xml", "json", "jsonp"]: _outfmt = "xml"

    if ('compress' in _kwargs) and (_kwargs['compress'] is not None):
        _compress = _kwargs['compress'].lower()
    else:
        _compress = request.REQUEST.get("compress", None) or "false"
        if _compress: _compress = _compress.lower()
    if _force_compress or _compress=="true":
        _compress = True
    else:
        _compress = False

    if ('callback' in _kwargs) and (_kwargs['callback'] is not None):
        _callback = _kwargs['callback']
    else:
        _callback = request.REQUEST.get("callback", "callback")

    if _outfmt=="xml":
        _buffer = loader.get_template(_template).render(_context)
        _mimetype = "text/xml"
    elif _outfmt=="json":
        _buffer = loader.get_template(_template).render(_context)
        # _temp = loader.get_template(_template).render(_context)
        # _buffer = xml2json(_temp, strip = 0)
        _mimetype = "application/json"
    elif _outfmt=="jsonp":
        _callback = escape(_callback)
        _temp1 = loader.get_template(_template).render(_context)
        _buffer=_temp1
        # _temp2 = xml2json(_temp1, strip = 0)
        # _buffer = "%s(%s)" % (_callback, _temp2)
        _mimetype = "text/plain"
    else:
        _buffer = "Not Implemented."
        _mimetype = "text/plain"
        _context["result"] = False
        _context["errorcode"]= ERROR_CODE.NOT_IMPLEMENTED
        _context["message"] = ERROR_MESSAGE.NOT_IMPLEMENTED
    tmp_buffer = _buffer[:]
    _buffer = tmp_buffer

    if _outfmt == "json":
        _buffer=xml2json(_buffer,strip = 0)
    if _outfmt == "jsonp":
        _temp2 = xml2json(_buffer, strip = 0)
        _buffer = "%s(%s)" % (_callback, _temp2)


    if _compress:
        response = compress_response(_buffer.encode("utf-8"))
    else:
        response = HttpResponse(_buffer, mimetype=_mimetype)

    try:
        if 'ats' in _context:
            key = 'ats'
        elif 'aos' in _context:
            key = 'aos'

        response["result"] = _context.get("result", _context[key].get('result'))
        response["errorcode"] = _context.get("errorcode", _context[key].get('code'))
        response["message"] = _context.get("message", _context[key].get('message'))
        response["timestamp"] = _context.get("timestamp", _context[key].get('timestamp'))
    except:
        pass

    return response
