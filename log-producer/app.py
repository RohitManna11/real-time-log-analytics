import os
import time
import random
import logging
from kafka import KafkaProducer

logging.basicConfig(level=logging.INFO)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "logs")

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

def generate_log_message():
    log_levels = ["INFO", "WARNING", "ERROR"]
    level = random.choice(log_levels)
    if level == "ERROR":
        return "ERROR: Something went wrong!"
    elif level == "WARNING":
        return "WARNING: This is a potential issue."
    else:
        return "INFO: All systems operational."

if __name__ == "__main__":
    logging.info(f"Starting log producer to topic {KAFKA_TOPIC}...")
    while True:
        message = generate_log_message()
        logging.info(f"Sending message: {message}")
        producer.send(KAFKA_TOPIC, message.encode("utf-8"))
        producer.flush()
        time.sleep(3)  # send a log every 3 seconds
