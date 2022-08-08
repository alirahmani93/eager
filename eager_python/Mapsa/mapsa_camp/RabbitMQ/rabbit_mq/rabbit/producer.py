import json
import os

import pika


class Producer:
    def __init__(self, host, username, password, port=5672):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(f'amqp://{username}:{password}@{host}:{port}'))
        self.channel = self.connection.channel()
        self.exchanges = []

    def produce(self, exchange, body, routing_key):
        if exchange not in self.exchanges:
            self.channel.exchange_declare(exchange=exchange)
            self.exchanges.append(exchange)

            self.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=body)


producer = Producer(
    host=os.environ.get("host"),
    port=int(os.environ.get("port")),
    username=os.environ.get("username"),
    password=os.environ.get("password"),
)
