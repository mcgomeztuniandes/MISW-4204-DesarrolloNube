from json import dumps
from kafka import KafkaProducer

class KafkaProducer():
    producer = KafkaProducer(
            bootstrap_servers = ['localhost:9092'],
            value_serializer=lambda m: dumps(m).encode('utf-8')
        )
    
    def enviarTarea(self, topic, keys, mensaje):
        self.producer.send(topic, key=bytes(keys, 'utf-8'), value = mensaje)
        self.producer.flush()