#!/bin/bash

venv/bin/gunicorn main:app --workers 12 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:9999
