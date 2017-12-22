#  install
openresty or ngnix
uwsgi
python 2.+
pip install -r requirements.txt

# celery
celery -A wxp worker --loglevel=info
