#!/bin/bash

# Activate virtual environment (optional)
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Load environment variables
export $(grep -v '^#' .env | xargs)

# Run FastAPI backend
echo "🚀 Starting FastAPI server..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
