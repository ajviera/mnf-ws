# FastNote Web Services

## Requirements
- _Python_ > 2.7

## Set up project

```sh
$ virtualenv mnf --python=python3
$ git clone git@github.com:ajviera/mnf-ws.git
$ source bin/activate
$ cd mnf-ws
$ pip install request
$ pip install -r requeriments.txt
```
### Start Server

In order to start the server on http://localhost:8000/ you will need to run:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```