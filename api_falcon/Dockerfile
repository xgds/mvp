FROM python:3.7
RUN pip install mongoengine pillow falcon gunicorn assertpy
RUN mkdir /api
COPY ./ /api
CMD cd /api && gunicorn -b 0.0.0.0:5000 --capture-output main:api
