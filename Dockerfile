FROM python:3.10.1-slim-bullseye

WORKDIR /python-executor

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]