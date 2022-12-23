include .env
export

# --- Common section ----------------------
some-sleep:
	sleep 3

rm-migrations-dirs:
	rm -rf mainapp/migrations
	rm -rf authapp/migrations
	rm -rf candidateapp/migrations
	rm -rf companyapp/migrations

clean-start-for-development:rm-migrations-dirs docker-down-remove-volumes docker-build-up \
some-sleep makemigrations migrate createsuperuser runserver

start-for-development: docker-down docker-build-up makemigrations migrate check-code runserver

# --------------------------------------------

# --- Poetry section ----------------------
poetry-shell:
	poetry shell
# --------------------------------------------

# --- Docker section ----------------------
docker-down:
	docker-compose -f docker-compose.yml down --remove-orphans

docker-down-remove-volumes:
	docker-compose -f docker-compose.yml down -v --remove-orphans

docker-up:
	docker-compose -f docker-compose.yml up -d

docker-build-up:
	docker-compose -f docker-compose.yml up -d --build

docker-logs:
	docker-compose -f docker-compose.yml logs -f

python-cli:
	docker exec -ti hh-agile-python-cli sh

python-cli-log:
	docker-compose -f docker-compose.yml logs -f python_container

# --------------------------------------------

# --- Django section ----------------------
flush-local:
	python manage.py flush --no-input

runserver-local:
	python manage.py runserver

makemigrations-local:
	python manage.py makemigrations mainapp
	python manage.py makemigrations authapp
	python manage.py makemigrations candidateapp
	python manage.py makemigrations companyapp

migrate-local:
	python manage.py migrate

createsuperuser-local:
	 python manage.py createsuperuser --no-input

collectstatic-local:
	python manage.py collectstatic --no-input

flush:
	docker-compose -f docker-compose.yml exec python_container python manage.py flush --no-input

runserver:
	docker-compose -f docker-compose.yml exec python_container python manage.py runserver

makemigrations:
	docker-compose -f docker-compose.yml exec python_container python manage.py makemigrations mainapp
	docker-compose -f docker-compose.yml exec python_container python manage.py makemigrations authapp
	docker-compose -f docker-compose.yml exec python_container python manage.py makemigrations candidateapp
	docker-compose -f docker-compose.yml exec python_container python manage.py makemigrations companyapp

migrate:
	docker-compose -f docker-compose.yml exec python_container python manage.py migrate

createsuperuser:
	docker-compose -f docker-compose.yml exec python_container python manage.py createsuperuser --no-input

collectstatic:
	docker-compose -f docker-compose.yml exec python_container python manage.py collectstatic --no-input
# --------------------------------------------

# --- Code section ----------------------
check-code:
	docker-compose -f docker-compose.yml exec python_container isort agile_hh/ candidateapp/ authapp/ companyapp/ mainapp/
	docker-compose -f docker-compose.yml exec python_container flake8 --extend-ignore E501,F401 agile_hh/ candidateapp/ authapp/ companyapp/ mainapp/
# --------------------------------------------