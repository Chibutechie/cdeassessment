FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the ETL code
COPY . .

# Default command to run the ETL pipeline
CMD ["python", "main.py"]
