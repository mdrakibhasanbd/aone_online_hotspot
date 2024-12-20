# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Set the environment variable for the time zone
# This is UTC+6. Change the time zone if needed.

ENV TZ=Asia/Dhaka

# Install tzdata to handle time zone setting and other dependencies
RUN apt-get update && \
    apt-get install -y tzdata && \
    rm -rf /var/lib/apt/lists/* && \
    dpkg-reconfigure -f noninteractive tzdata

# Copy only requirements.txt for dependency caching
COPY requirements.txt /app/

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y gcc python3-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade redis
# Copy the rest of the application code
COPY . /app/

# Expose the application port
EXPOSE 5008

# Run Gunicorn to serve the app
CMD ["gunicorn", "-w", "8", "-b", "0.0.0.0:5008", "--worker-connections", "1000", "--timeout", "60", "--worker-class", "gevent", "run_gunicorn:app"]
