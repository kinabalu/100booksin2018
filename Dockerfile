# Working from Python image
FROM python:3.6

WORKDIR /app/

COPY ./api ./app

# Update Python packages and install Python requirements
COPY requirements.txt /app/
RUN pip3 install -U pip && pip3 install -r requirements.txt && rm -rf /var/lib/apt/lists/*

ADD ./api/ /app/

EXPOSE 8080/tcp