#!/bin/bash
uvicorn app.main:app --host 0.0.0.0 --port $SERVER_PORT