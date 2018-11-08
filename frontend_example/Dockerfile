FROM ubuntu:latest
RUN  apt-get update && apt-get install -y curl nginx
RUN  apt-get install -y gnupg
RUN  cd / && curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
RUN  cd / && bash nodesource_setup.sh
RUN  apt-get update && apt-get install -y nodejs
COPY . /app
RUN  cd /app && npm install
RUN  cd /app && npm run build
RUN  rm -v /etc/nginx/nginx.conf
ADD  nginx.conf /etc/nginx/
RUN  ls /app
RUN  cp -R /app/dist/map/* /usr/share/nginx/html/
RUN  echo "daemon off;" >> /etc/nginx/nginx.conf
RUN  apt-get remove -y curl nodejs
CMD  service nginx start