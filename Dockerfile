FROM python:3.10

COPY . .

RUN pip install -r requirements.txt

WORKDIR /app

RUN ["chmod", "+x", "run_migrations.sh"]

# RUN piccolo migrations check

