# Server rest api
Rest api application for family server.

## Overview:
* Framework: Flask
* DB: SQLite3 

## Dev setup:
* Install poetry.
* Install depedency: `poetry install`
* Update `.env` file.
* Execute application: `poetry run python server_rest_api/app.py`
* Execute application: `cd server_rest_api; poetry run flask run --port 5001`
* Execution via `wsgi` server: `poetry run gunicorn`
* Instead of 5001; we can use different port, check the config file: `gunicorn.conf.py`.


## Deplyment into server:
* clone repo
* cd `family-server/server-rest-api`
* Build image `podman build -t server-rest-api:v1 .`
* Executing container: `podman run -d -p 5001:5001 --name sra server-rest-api:v1`

### Ngninx related
* edit : `/etc/nginx/sites-enabled/default`
* Add the location:
```
        location  /api/version {
                proxy_pass http://localhost:5001/version;
        }

        location /api/docs {
                proxy_pass http://localhost:5001/docs/;
        }

        location /docs {
                proxy_pass http://localhost:5001/docs/;
        }

        location /static/swagger.yaml {
                proxy_pass http://localhost:5001/static/swagger.yaml;
        }

```
* Port based on the defined in source code
