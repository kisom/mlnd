#!/bin/bash

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-5000}"

FLASK_APP="spam.py" flask run --host $HOST --port $PORT
