import matplotlib.pyplot as plt

# Leer los datos del archivo de texto del elefante
with open('./latency-oslo-700-1000-caract-0-seg.txt', 'r') as file:
    data_oslo = file.read().splitlines()
    data_oslo = [float(value) for value in data_oslo]

with open('./latency-rio-700-1000-caract-0-seg.txt', 'r') as file:
    data_rio = file.read().splitlines()
    data_rio = [float(value) for value in data_rio]

# with open('./700-1000c-0-seg/latency-chicago-700-1000-caract-0-seg.txt', 'r') as file:
#     data_chicago = file.read().splitlines()
#     data_chicago = [float(value) for value in data_chicago]

# with open('./700-1000c-0-seg/latency-dallas-700-1000-caract-0-seg.txt', 'r') as file:
#     data_dallas = file.read().splitlines()
#     data_dallas = [float(value) for value in data_dallas]

# with open('./700-1000c-0-seg/latency-denver-700-1000-caract-0-seg.txt', 'r') as file:
#     data_denver = file.read().splitlines()
#     data_denver = [float(value) for value in data_denver]


#all_data = data_oslo1 + data_oslo2 + data_oslo3;
# x_austin = list(range(1, len(data_austin) + 1))
# x_boston = list(range(1, len(data_boston) + 1))
# x_chicago = list(range(1, len(data_chicago) + 1))
x_oslo = list(range(1, len(data_oslo) + 1))
x_rio = list(range(1, len(data_rio) + 1))

# Crear la figura y los ejes del gráfico
fig, ax = plt.subplots()

ax.plot(x_oslo, data_oslo, color='red', label='oslo')
ax.plot(x_rio, data_rio, color='blue', label='rio')
# ax.plot(x_denver, data_denver, color='green', label='Denver')
# ax.plot(x_austin, data_austin, color='yellow', label='Austin')
# ax.plot(x_dallas, data_dallas, color='purple', label='Dallas')

# Configurar etiquetas del eje x y y
ax.set_xlabel('N° mensaje')
ax.set_ylabel('Tiempo (s)')

# Configurar título del gráfico
ax.set_title('Latencia en Kafka ( Data pesada 3-1 1-3 | 0 seg)')

# Agregar leyenda
ax.legend()

# Mostrar el gráfico
plt.show()