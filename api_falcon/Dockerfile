FROM python:3.7
RUN pip install mongoengine pillow falcon falcon-cors gunicorn
RUN mkdir /api
COPY ./ /api
CMD cd /api && gunicorn -b 0.0.0.0:5000 --workers 8 --capture-output main:api
