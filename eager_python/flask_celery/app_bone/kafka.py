import uuid
from flask_socketio import emit
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from socketio import *

BOOTSTRAP_SERVERS = "BOOTSTRAP_SERVERS"
TOPIC_NAME = "TOPIC_NAME"
from flask_socketio import SocketIO


@SocketIO.on('kafkaconsumer', namespace="/kafka")
def kafkaconsumer(message):
    consumer = KafkaConsumer(group_id='consumer-1',
                             bootstrap_servers=BOOTSTRAP_SERVERS)
    tp = TopicPartition(TOPIC_NAME, 0)
    consumer.assign([tp])
    consumer.seek_to_end(tp)
    lastOffset = consumer.position(tp)
    consumer.seek_to_beginning(tp)
    emit('kafkaconsumer1', {'data': ''})
    for message in consumer:
        emit('kafkaconsumer',
             {'data': message.value.decode('utf8')})
        if message.offset == lastOffset - 1:
            break
    consumer.close()


@SocketIO.on('kafkaproducer', namespace="/kafka")
def kafkaproducer(message):
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
    producer.send(TOPIC_NAME, value=bytes(str(message),
                                          encoding='utf-8'), key=bytes(str(uuid.uuid4()),
                                                                       encoding='utf-8'))
    emit('logs', {'data': 'Added ' + message + ' to topic'})
    emit('kafkaproducer', {'data': message})
    producer.close()
    kafkaconsumer(message)
