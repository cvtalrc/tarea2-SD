import random 
import string 
import time

def generate_message() -> dict:
    timestamp = time.time()
    data_size = random.randint(700, 1000)
    data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=data_size))
    velocidad_promedio = random.randint(20, 120)
    accidentes = random.randint(0, 5)
    return {
        'timestamp': timestamp,
        'values': {'velocidad': velocidad_promedio,
                   'accidentes': accidentes,
                   'data': data},
    }