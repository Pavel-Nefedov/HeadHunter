include .env
export

# --- Docker section ----------------------
docker-down:
	docker-compose -f docker-compose.yml down -v --remove-orphans

docker-build-up:
	docker-compose -f docker-compose.yml up -d --build

docker-logs:
	docker-compose -f docker-compose.yml logs -f
# --------------------------------------------

# --- Django section ----------------------
runserver:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	 python manage.py createsuperuser --noinput
# --------------------------------------------

# --- Code section ----------------------
check-code:
	isort agile_hh/
	flake8 --extend-ignore E501,F401 agile_hh/
# --------------------------------------------