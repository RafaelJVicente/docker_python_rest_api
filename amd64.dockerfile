FROM amd64/python:3-alpine

WORKDIR /usr/src/app
COPY app .
RUN pip install --no-cache-dir -r requirements.txt
CMD python rest_app.py