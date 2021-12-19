# pull official base image
FROM python:3.10

# set work directory
WORKDIR /support

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copying dependencies to working directory
RUN pip install --upgrade pip
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY src/ ./src

EXPOSE 8000