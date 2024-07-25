#!/bin/bash

# Install dependencies
python3.9 -m ensurepip --upgrade 

pip install -r requirements.txt

# Run any build commands
python3.9 manage.py collectstatic --noinput

