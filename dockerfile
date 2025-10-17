FROM python:3.13.9-slim

RUN mkdir /app/
COPY requirements.txt /app/
COPY ./setup.py /app/

COPY src/ /app/src/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install -e /app

# pytest requirements
WORKDIR /app/

CMD [ "pytest" ]
ENV PYTHONDONTWRITEBYTECODE=true