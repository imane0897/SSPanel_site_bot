FROM python:3.7-slim-buster

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

COPY . /opt/N3ROBot/
WORKDIR /opt/N3ROBot/

EXPOSE 8080
CMD ["python", "src/main.py"]