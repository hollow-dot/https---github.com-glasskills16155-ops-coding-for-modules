# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Copy project files
COPY . .

# Install dependencies only if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Default command to run your app
CMD ["python", "./app.py"]