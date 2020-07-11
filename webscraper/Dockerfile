FROM python:3.8
ENV PYTHONBUFFERED 1
RUN apt-get update && apt-get install -y netcat
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
