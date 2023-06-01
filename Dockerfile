FROM python:3.9.7-slim

COPY . /app
WORKDIR /app

RUN  python3 -m venv /opt/env

RUN /opt/env/bin/pip install -r requirements.txt

SHELL ["CMD", "/bin/bash", "-c"]
RUN source env/bin/activate
EXPOSE 8000
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]

