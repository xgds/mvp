FROM python:3.7
RUN pip install mongoengine pillow flask flask-restful flask-restful-swagger
COPY ./* /
WORKDIR /
ENTRYPOINT cd / && python /main.py