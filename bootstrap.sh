#!/bin/sh
export FLASK_APP=./rest-api/index.py
source $(python3 -m pipenv --venv)/bin/activate
python3 -m flask run -h 0.0.0.0