import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo de valores para a envergadura B
B = np.linspace(0.1, 6, 100)  # envergadura variando de 0.1 a 6 metros

# Calculando os valores de potência P correspondentes
P = 981.8 / (B**0.3995)

# Limitando P ao máximo permitido de 760W
P = np.minimum(P, 760)

# Função para validar as restrições
def valida_restricoes(H, B, P, N=2):
    if H <= 0.6 and B <= 2.5 and P <= 850 and N == 2:
        return True
    return False

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(B, P, label='Potência máxima permitida')

# Encontrando o ponto onde deixa de ser linear
linear_index = np.argmax(P < 760)
B_linear = B[linear_index]
P_linear = P[linear_index]

# Plotando o ponto onde a curva deixa de ser linear
plt.plot(B_linear, P_linear, 'ro', label=f'Descontinuidade ({B_linear:.2f}, {P_linear:.2f})')

plt.xlabel('Envergadura da Asa (B) [m]')
plt.ylabel('Potência (P) [W]')
plt.title('Gráfico de Potência vs Envergadura da Asa')
plt.legend()
plt.grid(True)
plt.show()

# Imprimindo os vetores de B e P
B_values = B.tolist()
P_values = P.tolist()

# Validando as restrições para cada par de valores (B, P)
validos = [valida_restricoes(0.6, b, p) for b, p in zip(B_values, P_values)]
pares_validos = list(zip(B_values, P_values, validos))

# Exibindo os pares válidos
for b, p, valido in pares_validos:
    if valido:
        print(f"Envergadura (B): {b:.2f} m, Potência (P): {p:.2f} W - Válido: {valido}")

# Salvando os resultados em um arquivo
with open('resultados.txt', 'w') as f:
    for b, p, valido in pares_validos:
        if valido:
            f.write(f"Envergadura (B): {b:.2f} m, Potência (P): {p:.2f} W - Válido: {valido}\n")

B_values, P_values
