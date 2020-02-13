FROM python:3

WORKDIR /usr/app

# copy requirements.txt and install dependencies first
# to optimize cache
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

COPY ./ ./

# default values
ENV FLASK_APP=setup.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=8080
ENV FLASK_CONFIG=dev-docker
ENV FLASK_RUN_HOST=0.0.0.0
ENV JWT_SECRET_KEY=secret_key
# to see print statements set to 1
ENV PYTHONUNBUFFERED=1

CMD ["flask", "run"]