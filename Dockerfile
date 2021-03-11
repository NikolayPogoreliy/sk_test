FROM nikolaik/python-nodejs:latest

WORKDIR /app
COPY . /app
RUN npm --prefix ./frontend clean-install
RUN npm --prefix ./frontend run build
RUN pip install -r requirements.txt
#RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
#RUN pg_config
#COPY . .

CMD uwsgi --module=prototype.wsgi --http=0.0.0.0:80