import numpy as np
import matplotlib.pyplot as plt

# Dados dos motores
motores = {
    "Hacker Motors A40-12L V4 kv410": {"potencia": 462.5, "empuxo": 1897.42, "rpm": 7585},
    "Scorpion SII-3026-890": {"potencia": 758.3, "empuxo": 3670.2, "rpm": 8564},
    "Cobra C4120/12": {"potencia": 670.1, "empuxo": 3265, "rpm": 7224}
}

# Constantes
densidade_ar = 1.225  # kg/m^3 ao nível do mar
eficiencia_helice = 0.6

# Função para calcular a tração disponível (Thrust)
def tracao_disponivel(potencia, eficiencia, densidade, diametro_helice, rpm):
    v = 0  # Velocidade de voo inicial
    return (eficiencia * potencia) / (v + ((rpm * diametro_helice) / 60) * np.pi)

# Definindo o intervalo de valores para a envergadura B
B = np.linspace(0.1, 2.5, 100)  # envergadura variando de 0.1 a 2.5 metros

# Função para calcular a potência máxima permitida pela equação
def potencia_maxima(B):
    return 981.8 / (B**0.3995)

# Calculando a potência necessária para cada valor de envergadura
P_necessaria = potencia_maxima(B)

# Determinando o motor mais ideal para cada envergadura
motores_ideais = []
for p in P_necessaria:
    motor_ideal = None
    for motor, dados in motores.items():
        if p <= dados["potencia"]:
            if motor_ideal is None or dados["empuxo"] > motores[motor_ideal]["empuxo"]:
                motor_ideal = motor
    motores_ideais.append(motor_ideal)

# Plotando o gráfico
plt.figure(figsize=(14, 8))

# Cores para os motores
cores = {
    "Hacker Motors A40-12L V4 kv410": "blue",
    "Scorpion SII-3026-890": "green",
    "Cobra C4120/12": "red"
}

# Plotando os gráficos de potência vs envergadura para cada motor
for motor, dados in motores.items():
    plt.plot(B, np.minimum(potencia_maxima(B), dados["potencia"]), 
             label=f'{motor} - Empuxo: {dados["empuxo"]} g', color=cores[motor], marker='o', markersize=4)

# Adicionando os motores ideais ao gráfico
for i, motor in enumerate(motores_ideais):
    if motor is not None:
        plt.annotate(motor, (B[i], P_necessaria[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color=cores[motor])

plt.xlabel('Envergadura da Asa (B) [m]')
plt.ylabel('Potência (P) [W]')
plt.title('Motor Ideal para Diferentes Tamanhos de Asas')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.show()

# Exibindo os resultados
for b, p, motor in zip(B, P_necessaria, motores_ideais):
    print(f"Envergadura (B): {b:.2f} m, Potência Necessária (P): {p:.2f} W - Motor Ideal: {motor}")

# Calculando a envergadura ideal
envergadura_ideal = 2.5
potencia_ideal = potencia_maxima(envergadura_ideal)
motor_ideal = "Scorpion SII-3026-890"

print("\nRecomendação Final:")
print(f"Motor Ideal: {motor_ideal}")
print(f"Envergadura Ideal: {envergadura_ideal} m")
print(f"Potência Necessária: {potencia_ideal:.2f} W")
