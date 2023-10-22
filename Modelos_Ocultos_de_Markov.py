# Definir el modelo HMM
num_estados = 2
num_simbolos = 3

# Matriz de transición de estado (A)
A = [[0.7, 0.3],
     [0.4, 0.6]]

# Probabilidades iniciales de estado
pi = [0.6, 0.4]

# Matriz de observación (B)
B = [[0.1, 0.4, 0.5],
     [0.7, 0.2, 0.1]]

# Secuencia de observaciones
observaciones = [0, 1, 2, 2, 1, 0]

# Inicialización
T = len(observaciones)
alpha = [[0.0] * T for _ in range(num_estados)]

# Algoritmo hacia adelante para calcular la probabilidad de la secuencia de observaciones
for t in range(T):
    for i in range(num_estados):
        if t == 0:
            alpha[i][t] = pi[i] * B[i][observaciones[t]]
        else:
            alpha[i][t] = B[i][observaciones[t]] * sum(alpha[j][t - 1] * A[j][i] for j in range(num_estados))

# Probabilidad de la secuencia de observaciones
probabilidad = sum(alpha[i][-1] for i in range(num_estados))

print("Probabilidad de la secuencia de observaciones:", probabilidad)

