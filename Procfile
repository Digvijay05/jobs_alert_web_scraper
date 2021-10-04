web: gunicorn jadavjobs_admin.wsgi --timeout 200 --keep-alive 20
worker: python manage.py crontab add && python manage.py crontab show