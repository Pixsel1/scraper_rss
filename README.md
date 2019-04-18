# Scraper_rss
Scraper_rss is a Django based application, which import currency rates from ECB, save in database and serve via REST API in JSON format.

1. Clone repository
2. `cd` into project
3. Run `docker-compose build`
4. Run `docker-compose run django python manage.py migrate`
5. Run `docker-compose up` to run the application

# Architecture
Simple application that does not require a lot of logic. In this case, we use the traditional architecture solution which Django give us.

We use:
 - Docker
 - PostgreSQL
 - Celery
 - RabbitMQ as a message broker

# Tests
To run the tests, use the command:
docker-compose run django python manage.py test
