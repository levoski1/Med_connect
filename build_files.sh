#!/bin/bash

# Install dependencies
python3.9 -m pip install --upgrade pip
pip install -r requirements.txt

# Run any build commands
python3 manage.py collectstatic --noinput
python3 manage.py migrate
