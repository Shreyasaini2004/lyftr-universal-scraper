#!/bin/bash
set -e

python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
playwright install chromium

cd frontend
npm install
npm run build
cd ..

uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
