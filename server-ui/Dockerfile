FROM python:3.8-slim
WORKDIR /server-ui

COPY run.sh .
RUN  chmod +x run.sh

COPY ./dist/server-ui/browser/ .

ENTRYPOINT ["./run.sh"]
