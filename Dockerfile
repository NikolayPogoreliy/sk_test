FROM nikolaik/python-nodejs:latest

WORKDIR /app
COPY . /app
RUN npm clean-install
RUN npm run build
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD uwsgi --module=backend.wsgi --http=0.0.0.0:80