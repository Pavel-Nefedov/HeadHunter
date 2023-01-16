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

# Сначала запусти виртуальную среду
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

migrate:
	python manage.py migrate

createsuperuser:
	 python manage.py createsuperuser --no-input

collectstatic:
	python manage.py collectstatic --no-input

parse_news:
	python manage.py parse_news

test:
	python manage.py test

add_fake_users:
	python manage.py add_fake_users 10


# --------------------------------------------

# --- Code section ----------------------
check-code:
	isort agile_hh/ candidateapp/ authapp/ companyapp/ mainapp/
	flake8 --extend-ignore E501,F401 agile_hh/ candidateapp/ authapp/ companyapp/ mainapp/
# --------------------------------------------