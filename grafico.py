import matplotlib.pyplot as plt
import numpy as np

x_valores = np.linspace(0, 49.9, 500)

y_valores = 1000 / (50 - x_valores)

plt.figure(figsize=(10, 6))

plt.plot(x_valores, y_valores, label='T(x) = 1000 / (50 - x)')

plt.axvline(
    x=50,
    linestyle='--',
    label='Assíntota x = 50'
)

plt.xlabel('Requisições por segundo')
plt.ylabel('Tempo médio de resposta (ms)')
plt.title('Tempo de resposta da API em função da carga')

plt.legend()
plt.grid(True)

plt.show()