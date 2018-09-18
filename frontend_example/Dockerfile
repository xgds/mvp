FROM node:latest

RUN  mkdir /app
COPY ./* /app/
COPY ./src /app/src
RUN  cd /app && npm install . && npm run build

RUN  apt-get update && \
     apt-get install -y software-properties-common

RUN  add-apt-repository ppa:nginx/stable && \
     apt-get update && \
     apt-get install -y nginx

CMD  /usr/bin/nginx -c /app/nginx.conf