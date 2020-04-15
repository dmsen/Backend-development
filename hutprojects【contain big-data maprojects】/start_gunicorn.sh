cd /django/dmseng
/usr/local/bin/gunicorn -w 4 -b 127.0.0.1:8000 -D --access-logfile=/tmp/gunicorn.log dmseng.wsgi
