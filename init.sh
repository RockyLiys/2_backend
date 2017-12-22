rm db.sqlite3
rm adapter/migrations/00*
python manage.py makemigrations
cp 0002_auto_20171124_0319.py adapter/migrations/
python manage.py migrate
python manage.py create_admin
python manage.py init_data
