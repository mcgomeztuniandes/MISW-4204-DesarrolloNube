from json import loads
from kafka import KafkaConsumer
from convertir.convert import ConvertirAudio
import os

class KafkaConsumer():
    server = os.environ.get('SERVER_KAFKA', None)
    if server == None:
        server = 'localhost:9092'

    consumer = KafkaConsumer(
        'Tareas',
        bootstrap_servers = [server],
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
    )
    
    def recibirTareas(self):
        convertidor_audio = ConvertirAudio()
        for t in self.consumer:
            convertidor_audio.convert_manage(t.value)
            


