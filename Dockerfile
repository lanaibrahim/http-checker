FROM python:slim-buster

ENV FLASK_APP=http_checker.py

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 4999

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=4999"]%