FROM debian

MAINTAINER Ryan Vacek

RUN apt-get install bash

FROM python:3.8

EXPOSE 500

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python apiserver.py"]
