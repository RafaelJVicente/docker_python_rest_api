FROM python:3-alpine

WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/rest_app.py .

ENTRYPOINT [ "python" ]
CMD [ "rest_app.py" ]
