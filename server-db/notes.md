# Important notes

## connection info
* set password: `export PGPASSWORD=<pass>`
* connection manual: `psql -d family_server_db -U <user_name> -h localhost`
* connection with sql script: `psql -U <user_name> -d family_server_db -f family_server_db_psql.sql`

## creating all schema
* execute: `./create_schema.sh`