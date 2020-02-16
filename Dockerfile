FROM python:3

COPY src/ ./

CMD [ "python", "./Server.py"]
