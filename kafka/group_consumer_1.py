from confluent_kafka import Consumer

if __name__ == '__main__':

    conf = {
    'bootstrap.servers': 'localhost:9092',  # Dirección de los brokers de Kafka
    'group.id': 'street1',  # Identificador del grupo de consumidores
    'auto.offset.reset': 'earliest',  # Configuración de inicio de lectura de los mensajes
    'enable.auto.commit': False  # Desactivar la confirmación automática de offsets
    }

    consumer = Consumer(conf)

    topic = 'orlando'
    consumer.subscribe([topic])

    print("Escuchando en orlando | group id: street1")
    try:
        while True:
            msg = consumer.poll(1.0) 

            if msg is None:
                continue

            print('Mensaje recibido: {}'.format(msg.value()))

            consumer.commit(msg)

    except KeyboardInterrupt:
        pass