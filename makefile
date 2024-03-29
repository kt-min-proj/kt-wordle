all: makemigration migrate runserver

makemigration:
	python manage.py makemigrations --merge

migrate:
	python manage.py migrate --fake
	python manage.py migrate

runserver:
	python manage.py runserver

shell:
	python manage.py shell
