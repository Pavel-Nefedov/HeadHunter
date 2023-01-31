include .env
export

# --- Common section ----------------------
start: docker-down docker-up runserver

stop: docker-down

some-sleep:
	sleep 3

rm-migrations-dirs:
	rm -rf mainapp/migrations
	rm -rf authapp/migrations
	rm -rf candidateapp/migrations
	rm -rf companyapp/migrations

rm-data-dirs:
	rm -rf mainapp/management/data

clean-start-for-non-docker-development:rm-migrations-dirs rm-data-dirs docker-down-remove-volumes docker-build-up \
some-sleep makemigrations migrate createsuperuser parse_news add_fake_users runserver

clean-start-for-docker-development:rm-migrations-dirs rm-data-dirs docker-down-remove-volumes docker-build-up \
some-sleep docker-makemigrations docker-migrate docker-createsuperuser add_moderator_user docker-parse_news \
docker-add_fake_users

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

docker-build:
	docker-compose build

docker-build-up:
	docker-compose -f docker-compose.yml up -d --build

docker-logs:
	docker-compose -f docker-compose.yml logs -f

# --------------------------------------------

# --- Django section ----------------------
flush:
	python manage.py flush --no-input

runserver:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations mainapp
	python manage.py makemigrations authapp
	python manage.py makemigrations candidateapp
	python manage.py makemigrations companyapp

docker-makemigrations:
	docker-compose run --rm web-app sh -c "python manage.py makemigrations mainapp"
	docker-compose run --rm web-app sh -c "python manage.py makemigrations authapp"
	docker-compose run --rm web-app sh -c "python manage.py makemigrations candidateapp"
	docker-compose run --rm web-app sh -c "python manage.py makemigrations companyapp"

migrate:
	python manage.py migrate

docker-migrate:
	docker-compose run --rm web-app sh -c "python manage.py migrate"

createsuperuser:
	 python manage.py createsuperuser --no-input

docker-createsuperuser:
	docker-compose run --rm web-app sh -c "python manage.py createsuperuser --no-input"

collectstatic:
	python manage.py collectstatic --no-input

parse_news:
	python manage.py parse_news

docker-parse_news:
	docker-compose run --rm web-app sh -c "python manage.py parse_news"

add_fake_users:
	python manage.py add_fake_users 15

docker-add_fake_users:
	docker-compose run --rm web-app sh -c "python manage.py add_fake_users 15"

add_moderator_user:
	docker-compose run --rm web-app sh -c "python manage.py add_moderator_user"

# --------------------------------------------

# --- QA(testing) section ----------------------
# !For successful testing enter DEBUG = False in settings.py!
smoke_test:
	python manage.py test tests.mainapp.tests_main_smoke --debug-mode

test_mainapp_models:
	python manage.py test tests.mainapp.tests_main_models

test_companyapp_models:
	python manage.py test tests.companyapp.tests_company_models

test_user_management:
	python manage.py test authapp.tests.TestUserManagement

all_tests:
	python manage.py test tests.mainapp.tests_main_smoke
	python manage.py test tests.mainapp.tests_main_model

test:
	python manage.py test
# --------------------------------------------

# --- Code section ----------------------
check-code:
	isort agile_hh/ candidateapp/ authapp/ companyapp/ mainapp/
	flake8 --extend-ignore E501,F401 agile_hh/ candidateapp/ authapp/ companyapp/ mainapp/
# --------------------------------------------