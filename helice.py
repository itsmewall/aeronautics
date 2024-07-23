import numpy as np
import matplotlib.pyplot as plt

# Dados dos motores e hélices
motores = {
    "Hacker Motors A40-12L V4 kv410": {"potencia": 462.5, "rpm": 7585},
    "Scorpion SII-3026-890": {"potencia": 758.3, "rpm": 8564},
    "Cobra C4120/12": {"potencia": 670.1, "rpm": 7224}
}

helices = {
    "APC 12x8E": {"diametro": 0.305, "eficiencia": 0.6},
    "APC 15x4E": {"diametro": 0.381, "eficiencia": 0.65},
    "APC 15x8E": {"diametro": 0.381, "eficiencia": 0.7}
}

# Constantes
densidade_ar = 1.225  # kg/m^3 ao nível do mar

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

# Determinando a melhor combinação de motor e hélice para cada envergadura
combinacoes_ideais = []
for p in P_necessaria:
    melhor_combinacao = None
    for motor, dados_motor in motores.items():
        for helice, dados_helice in helices.items():
            if p <= dados_motor["potencia"]:
                tracao = tracao_disponivel(dados_motor["potencia"], dados_helice["eficiencia"], densidade_ar, dados_helice["diametro"], dados_motor["rpm"])
                if melhor_combinacao is None or tracao > melhor_combinacao["tracao"]:
                    melhor_combinacao = {"motor": motor, "helice": helice, "tracao": tracao}
    combinacoes_ideais.append(melhor_combinacao)

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
             label=f'{motor}', color=cores[motor], marker='o', markersize=4)

# Adicionando as combinações ideais ao gráfico
for i, combinacao in enumerate(combinacoes_ideais):
    if combinacao is not None:
        label = f'{combinacao["motor"]} com {combinacao["helice"]}'
        plt.annotate(label, (B[i], P_necessaria[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color=cores[combinacao["motor"]])

plt.xlabel('Envergadura da Asa (B) [m]')
plt.ylabel('Potência (P) [W]')
plt.title('Combinação Ideal de Motor e Hélice para Diferentes Tamanhos de Asas')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.show()

# Exibindo os resultados
for b, p, combinacao in zip(B, P_necessaria, combinacoes_ideais):
    if combinacao:
        print(f"Envergadura (B): {b:.2f} m, Potência Necessária (P): {p:.2f} W - Combinação Ideal: {combinacao['motor']} com {combinacao['helice']} (Tração: {combinacao['tracao']:.2f} N)")

# Calculando a envergadura ideal
envergadura_ideal = 2.5
potencia_ideal = potencia_maxima(envergadura_ideal)
motor_ideal = "Scorpion SII-3026-890"
helice_ideal = "APC 15x8E"

print("\nRecomendação Final:")
print(f"Motor Ideal: {motor_ideal}")
print(f"Hélice Ideal: {helice_ideal}")
print(f"Envergadura Ideal: {envergadura_ideal} m")
print(f"Potência Necessária: {potencia_ideal:.2f} W")
