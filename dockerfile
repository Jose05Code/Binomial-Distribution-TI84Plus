FROM python:3.7.6-buster

RUN pip install --upgrade pip

# pytest requirements
WORKDIR /app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "pytest" ]

