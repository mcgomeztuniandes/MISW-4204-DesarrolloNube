from json import dumps
from kafka import KafkaProducer
import os

class KafkaProducer():
    server = os.environ.get('SERVER_KAFKA', None)
    if server == None:
        server = 'localhost:9092'

    producer = KafkaProducer(
            bootstrap_servers = [server],
            value_serializer=lambda m: dumps(m).encode('utf-8')
        )
    
    def enviarTarea(self, topic, keys, mensaje):
        self.producer.send(topic, key=bytes(keys, 'utf-8'), value = mensaje)
        self.producer.flush()