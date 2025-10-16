FROM python:3.7.6-buster

RUN pip install --upgrade pip

# pytest requirements
RUN mkdir /app/
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

WORKDIR /app/

CMD [ "pytest" ]

