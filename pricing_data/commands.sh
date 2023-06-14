#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py load_regions
python3 manage.py load_sku_and_price
python3 manage.py load_benchmark_vm
