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
* Execution via `wsgi` server: `poetry run gunicorn`
* Instead of 5001; we can use different port, check the config file: `gunicorn.conf.py`.


## Deplyment into server:
* clone repo

### Building and deploying container
* Write the steps

### Ngninx related
* edit : `/etc/nginx/sites-enabled/default`
* Add the location:
```
        location /api/ {
                proxy_pass http://localhost:5001/;
        }
```
* Port based on the defined in source code
