import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo de valores para a envergadura B
B = np.linspace(0.1, 10, 100)  # envergadura variando de 0.1 a 2.5 metros

# Calculando os valores de potência P correspondentes
P = 981.8 / (B**0.3995)

# Limitando P ao máximo permitido de 850W
P = np.minimum(P, 758.3)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(B, P, label='Potência máxima permitida')
plt.xlabel('Envergadura da Asa (B) [m]')
plt.ylabel('Potência (P) [W]')
plt.title('Gráfico de Potência vs Envergadura da Asa')
plt.legend()
plt.grid(True)
plt.show()

# Fornecendo os vetores de B e P para cálculo preciso
B_values = B.tolist()
P_values = P.tolist()

B_values, P_values
