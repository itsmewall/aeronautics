import numpy as np
import matplotlib.pyplot as plt

# CONSTANTES
densidade_ar = 1.225  # kg/m^3 ao nível do mar
gravidade = 9.81  # m/s²

# VARIAVEIS
massa = 4.7  # Massa (kg)
S = 0.8   # Área da asa em (m^2)
C_Lmax = 1.6  # Coeficiente de sustentação máximo (CL_Max)
C_D = 0.035  # Coeficiente de arrasto (CD)
P = 785.3   # Potência do motor em Watts (W)
eta = 0.75   # Eficiência da hélice (entre 0 e 1)
v = 15.0    # Velocidade da aeronave em m/s (estimativa inicial para cálculo de tração)

# CALCULO DA TRAÇÃO ESTÁTICA
def tracao_estatica(P, eta, v):
    return (P * eta) / v

# VELOCIDADE MÁXIMA
def velocidade_maxima(T, S, C_D):
    return np.sqrt((2 * T) / (densidade_ar * S * C_D))

# VELOCIDADE DE CRUZEIRO
def velocidade_cruzeiro(v_max):
    return 0.9 * v_max

# VELOCIDADE DE DECOLAGEM
def velocidade_decolagem(massa, S, C_Lmax):
    W = massa * gravidade
    return 1.2 * np.sqrt((2 * W) / (densidade_ar * S * C_Lmax))

# VELOCIDADE DE SUSTENTAÇÃO
def velocidade_sustentacao(T, S, C_D):
    return np.sqrt((2 * T) / (densidade_ar * S * C_D))

# CALCULO DA TRAÇÃO
T = tracao_estatica(P, eta, v)

# CALCULO DA VELOCIDADE MÁXIMA
v_max = velocidade_maxima(T, S, C_D)

# CALCULO DE VELOCIDADES
v_cru = velocidade_cruzeiro(v_max)
v_lo = velocidade_decolagem(massa, S, C_Lmax)
v_sus = velocidade_sustentacao(T, S, C_D)

# RESULTADOS
print(f"Tração Estática (T): {T:.2f} N")
print(f"Velocidade Máxima (v_max): {v_max:.2f} m/s", f"km/h: {v_max * 3.6}" )
print(f"Velocidade de Cruzeiro (v_cru): {v_cru:.2f} m/s")
print(f"Velocidade de Decolagem (v_lo): {v_lo:.2f} m/s")
print(f"Velocidade de Sustentação (v_sus): {v_sus:.2f} m/s")

# GRAFICOS
velocidades = [v_max, v_cru, v_lo, v_sus]
labels = ['Máxima', 'Cruzeiro', 'Decolagem', 'Sustentação']

plt.figure(figsize=(10, 6))
plt.plot(labels, velocidades, marker='o', linestyle='-', color='b')
plt.xlabel('Tipo de Velocidade')
plt.ylabel('Velocidade (m/s)')
plt.title('Velocidades da Aeronave')
plt.grid(True)
plt.show()