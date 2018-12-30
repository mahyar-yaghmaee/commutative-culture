FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3-pip python3-dev build-essential -y

# add source file
COPY . /app
ENV HOME=/app
WORKDIR /app

# install python web server and dependencies
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "main:app"]
