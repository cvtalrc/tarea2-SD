import time 
import json 
from data_generator import generate_message
from kafka import KafkaProducer


def serializer(message):
    return json.dumps(message).encode('utf-8')

# Configuración Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    topic = input("Topic: ")
    total_msg= 18405
    contador=0
    while contador < total_msg:
        # Generando mensaje
        dummy_message = generate_message()
        
        # Enviando mensaje generado
        print(f'Enviando: {str(dummy_message)}')
        producer.send(topic, dummy_message)
        producer.flush()    

        contador=contador+1

        # time.sleep(intervalo)
        # tiempo_transcurrido += intervalo
        
        # time_to_sleep = 2
        # time.sleep(time_to_sleep)

