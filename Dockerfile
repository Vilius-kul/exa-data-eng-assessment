FROM python:3.10

COPY . .

RUN pip install -r requirements.txt

WORKDIR /app

RUN ["chmod", "+x", "run_migrations.sh"]




#bash -c "sh app/run_migrations.sh && python app/main.py "
