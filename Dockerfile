# Pull the base image of Python
FROM python:3.11.7-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set work directory
WORKDIR /HitHub

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the project
COPY . .