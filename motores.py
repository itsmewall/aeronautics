import numpy as np
import matplotlib.pyplot as plt

# Dados dos motores
motores = {
    "Hacker Motors A40-12L V4 kv410": {"potencia": 462.5, "empuxo": 1897.42},
    "Scorpion SII-3026-890": {"potencia": 758.3, "empuxo": 3670.2},
    "Cobra C4120/12": {"potencia": 670.1, "empuxo": 3265}
}

# Definindo o intervalo de valores para a envergadura B
B = np.linspace(0.1, 10, 100)  # envergadura variando de 0.1 a 2.5 metros

# Função para calcular a potência máxima permitida pela equação
def potencia_maxima(B):
    return 981.8 / (B**0.3995)

# Plotando o gráfico
plt.figure(figsize=(12, 8))

for motor, dados in motores.items():
    P = np.minimum(potencia_maxima(B), dados["potencia"])
    plt.plot(B, P, label=f'{motor} - Empuxo: {dados["empuxo"]} g')

plt.xlabel('Envergadura da Asa (B) [m]')
plt.ylabel('Potência (P) [W]')
plt.title('Gráfico de Potência vs Envergadura da Asa para Diferentes Motores')
plt.legend()
plt.grid(True)
plt.show()

# Calculando a maior envergadura possível para cada motor
maiores_asas = {}
for motor, dados in motores.items():
    B_possivel = B[np.where(potencia_maxima(B) <= dados["potencia"])[0][-1]]
    maiores_asas[motor] = B_possivel

print("Maiores Envergaduras Possíveis para Cada Motor:")
for motor, envergadura in maiores_asas.items():
    print(f"{motor}: {envergadura:.2f} m")