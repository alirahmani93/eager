import os

import pika
import json


class Consumer:
    def __init__(self, host, username, password, port=5672):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def _init_channel(self):
        conection = pika.BlockingConnection(parameters=pika.ConnectionParameters(
            host=f"amqp://{self.username}:{self.password}@{self.host}:{self.port}"))
        return conection.channel()

    def _init_queue(self, exchange, queue_name, routing_key):
        channel = self._init_channel()
        queue = channel.queue_declare(queue=queue_name)
        result = channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key)
        return result

    def consume(self, exchange, queue_name, routing_key, callback):
        channel = self._init_channel()
        queue = self._init_queue(exchange=exchange, queue_name=queue_name, routing_key=routing_key)
        channel.basic_consume(queue=queue, on_message_callback=callback)


consumer = Consumer(
    host=os.environ.get("host"),
    port=int(os.environ.get("port")),
    username=os.environ.get("username"),
    password=os.environ.get("password"),
)
