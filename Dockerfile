# Base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ ./src/
COPY data/ ./data/
COPY notebooks/ ./notebooks/

# Expose the port
EXPOSE 8000

# Run the application (example: using Flask or FastAPI)
CMD ["python", "-m", "src.main"]
