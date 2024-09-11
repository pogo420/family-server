# For dev only: export PATH=/Library/PostgreSQL/16/bin/:$PATH
psql -h localhost -d family_server_db -U db_manager -f family_server_db_psql.sql
