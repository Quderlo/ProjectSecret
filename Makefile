start-venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

migrate:
	venv/bin/python3 manage.py makemigrations statistic soldier equipment tasks
	venv/bin/python3 manage.py migrate

entry:
	export DJANGO_SETTINGS_MODULE=config.settings && venv/bin/python3 entrypoint.py

startapp: start-venv migrate start-venv