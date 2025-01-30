FROM python:3.9-slim

WORKDIR /app

# Install kafka-python library
RUN pip install kafka-python

COPY app.py /app/

CMD ["python", "app.py"]
