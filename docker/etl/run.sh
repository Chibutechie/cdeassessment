#!/bin/bash

# run.sh
# Bash script to run the Python ETL pipeline

echo "Starting ETL pipeline..."

# Activate Python virtual environment (adjust path if needed)
if [ -d "./venv" ]; then
    echo "Activating virtual environment..."
    source ./venv/bin/activate
else
    echo "Virtual environment not found. Make sure to create one."
fi

# Run extraction and transformation
echo "Running main ETL script..."
python3 main.py

# Check if the script ran successfully
if [ $? -eq 0 ]; then
    echo "ETL pipeline completed successfully!"
else
    echo "ETL pipeline failed. Check the logs for details."
fi

# Deactivate virtual environment if it was activated
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
fi

echo "Done."