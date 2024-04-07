FROM python:3.10-alpine

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
