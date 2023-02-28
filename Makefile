run:
	python manage.py runserver

make:
	python manage.py makemigrations

migrate:
	python manage.py migrate

admin:
	python manage.py createadmin

teams:
	python manage.py createteams

weeks:
	python manage.py createweeks

season:
	python manage.py createseason
