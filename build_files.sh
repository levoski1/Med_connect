#!/bin/bash

# Install dependencies
python3 -m ensurepip --upgrade 

pip install -r requirements.txt

# Run any build commands
python3 manage.py collectstatic --noinput
python3 manage.py migrate
