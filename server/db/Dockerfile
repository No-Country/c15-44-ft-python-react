# pull official base image
FROM postgres:15

# run create.sql on init
COPY create.sql /docker-entrypoint-initdb.d
