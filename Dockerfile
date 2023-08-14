FROM python:3.11


WORKDIR /eveonline-discord-relay

COPY requirements.txt .
COPY ./src ./src


RUN pip install -r requirements.txt

CMD ["python", "./src/eveintel.py"]