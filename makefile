# bin/sh

start: init-db start-app

init-db:
	@if [ ! -d "migrations" ]; then \
		export FLASK_ENV=development && export FLASK_APP=crud_flask && flask db init; \
	fi
	export FLASK_ENV=development && export FLASK_APP=crud_flask && flask db migrate && flask db upgrade

start-app:
	export FLASK_ENV=development && export FLASK_APP=crud_flask && python app.py
