FROM node:latest

RUN mkdir /app
COPY ./* /app/
COPY ./src /app/src
RUN cd /app && npm install .

CMD cd /app && npm run start