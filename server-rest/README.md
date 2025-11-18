# Rest server

* FastApi based family rest server

## For development:

* For dev server:

```
poetry run uvicorn server_rest.main:app --reload
```

* To extract requirements from poetry:

`poetry export -f requirements.txt --output requirements.txt --without-hashes`

## For server deployment:

* Execute: `./run_prod_server.sh`
