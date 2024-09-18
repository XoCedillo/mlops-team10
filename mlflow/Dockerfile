# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

