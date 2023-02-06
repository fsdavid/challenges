FROM nginx:stable-alpine

COPY ["../echo-connection-script.sh", "/docker-entrypoint.d/echo-connection-script.sh"]
RUN chown nginx:nginx /docker-entrypoint.d/echo-connection-script.sh

