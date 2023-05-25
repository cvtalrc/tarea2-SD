import json 
from kafka import KafkaConsumer
import time

if __name__ == '__main__':
    topic = input("Topic: ")
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest' #earliest
    )


    print(f'Escuchando en {topic}')
    for message in consumer:
        message_recived = json.loads(message.value)
        received_time = time.time()
        latency = float(received_time) - float(message_recived["timestamp"]) 
        file_name = "latency-" + topic + "-700-1000-caract-0-seg.txt"
        with open(file_name, 'a') as archivo:
            archivo.writelines(str(latency) + '\n')

        print(message_recived)
        #print(f'Latencia: ', latency)