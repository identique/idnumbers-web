#!/bin/bash
uvicorn app.main:app --host 0.0.0.0 --port $SERVER_PORT  --log-config ./app/logging_config.yaml