#!/bin/bash
gunicorn pricing_data.wsgi:application --config gunicorn.conf.py 
# python3 manage.py runserver 0:8000