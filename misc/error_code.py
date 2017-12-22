# -*- coding: utf-8  -*-
from django.utils.translation import ugettext as _
BASE_ERROR_CODE = 0x000000

class ERROR_CODE:
    '''
    class that gives definition of error code
    '''
    UNKNOWN_ERROR                     = BASE_ERROR_CODE + 0
    SUCCESS                           = BASE_ERROR_CODE + 1
    FAILURE                           = BASE_ERROR_CODE + 2
    PARAMETERS_ERROR                  = BASE_ERROR_CODE + 3
    SIGNATURE_ERROR                   = BASE_ERROR_CODE + 4
    LICENSE_IS_EXPIRED                = BASE_ERROR_CODE + 5
    NOT_IMPLEMENTED                   = BASE_ERROR_CODE + 6
    NOT_FOUND                         = BASE_ERROR_CODE + 7
    MULTI_FOUND                       = BASE_ERROR_CODE + 8
    HTTP_BODY_EMPTY                   = BASE_ERROR_CODE + 9
    XML_SYNTAX_ERROR                  = BASE_ERROR_CODE + 10
    REQUEST_METHOD_ERROR              = BASE_ERROR_CODE + 11
    NOLOGIN                           = BASE_ERROR_CODE + 12
    PERMISSION_DENIED                 = BASE_ERROR_CODE + 13
    STORAGE_IS_FULL                   = BASE_ERROR_CODE + 14
    DATA_SOURCE_FAILURE               = BASE_ERROR_CODE + 15            # For external real time access request, like stock or violation.
    TOO_HIGH_RATE                     = BASE_ERROR_CODE + 16
    '''
    account
    '''
    ACCOUNT_NOLOGIN                   = BASE_ERROR_CODE + 100
    ACCOUNT_INVALIDUSERNAMEORPASSWORD = BASE_ERROR_CODE + 101
    ACCOUNT_USERNAME_ALREADY_EXIST    = BASE_ERROR_CODE + 102
    ACCOUNT_USERNAME_NOT_EXIST        = BASE_ERROR_CODE + 103
    ACCOUNT_REGISTER_PARAMETERS_ERROR = BASE_ERROR_CODE + 104
    ACCOUNT_LOGIN_PARAMETERS_ERROR    = BASE_ERROR_CODE + 105
    ACCOUNT_UPDATEPASSWD_INVALIDPASSWD= BASE_ERROR_CODE + 106
    ACCOUNT_UPDATEPASSWD_PARAM_ERROR  = BASE_ERROR_CODE + 107
    ACCOUNT_RESETPASSWD_TOO_FREQUENT  = BASE_ERROR_CODE + 108
    ACCOUNT_LOGIN_ERROR               = BASE_ERROR_CODE + 109
    ACCOUNT_NO_PERMISSION             = BASE_ERROR_CODE + 110

class ERROR_MESSAGE:
    '''
    class that gives definition of error message
    '''
    UNKNOWN_ERROR                     = _('Unexpected error.')
    SUCCESS                           = _('Successful.')
    FAILURE                           = _('Failure.')
    PARAMETERS_ERROR                  = _('Params error.')
    SIGNATURE_ERROR                   = _('Signature verification failed.')
    LICENSE_IS_EXPIRED                = _('Sorry, your license has expired.')
    NOT_IMPLEMENTED                   = _('Not Implemented.')
    NOT_FOUND                         = _('Not found.')
    MULTI_FOUND                       = _('Multi-found.')
    HTTP_BODY_EMPTY                   = _('HTTP body empty.')
    XML_SYNTAX_ERROR                  = _('XML format error.')
    REQUEST_METHOD_ERROR              = _('Request method not supported.')
    NOLOGIN                           = _('Not login.')
    PERMISSION_DENIED                 = _('Sorry, Permission Denied.')
    STORAGE_IS_FULL                   = _('Sorry, Storage is full.')
    DATA_SOURCE_FAILURE               = _('Data source request failure.')
    TOO_HIGH_RATE                     = _('Too high rate')
    '''
    account
    '''
    ACCOUNT_NOLOGIN                   = _('Not login.')
    ACCOUNT_INVALIDUSERNAMEORPASSWORD = _('Sorry, your username must be between 3 and 100 characters long, and Password must be greater than 6 characters.')
    ACCOUNT_USERNAME_ALREADY_EXIST    = _('Username already existed.')
    ACCOUNT_USERNAME_NOT_EXIST        = _('Username not exist.')
    ACCOUNT_REGISTER_PARAMETERS_ERROR = _('You must input username and password')
    ACCOUNT_LOGIN_PARAMETERS_ERROR    = _('Sorry, your username must be between 3 and 100 characters long, and Password must be greater than 6 characters.')
    ACCOUNT_UPDATEPASSWD_INVALIDPASSWD= _('User update password is failure.')
    ACCOUNT_UPDATEPASSWD_PARAM_ERROR  = _('You must enter the correct old password and a valid new password.')
    ACCOUNT_RESETPASSWD_TOO_FREQUENT  = _('Sorry, too often to reset your password.')
    ACCOUNT_LOGIN_ERROR               = _('Invalid username or password.')
    ACCOUNT_NO_PERMISSION             = _('Sorry, operation not allowed.')
