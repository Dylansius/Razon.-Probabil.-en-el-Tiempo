import random

# Función de transición de estado
def transicion_estado(estado_anterior):
    # Simulación de movimiento del objeto
    ruido_transicion = random.gauss(0, 0.1)  # Ruido de la transición
    nuevo_estado = estado_anterior + 1 + ruido_transicion
    return nuevo_estado

# Función de observación
def observacion(estado):
    # Simulación de medición
    ruido_observacion = random.gauss(0, 1)  # Ruido de la observación
    return estado + ruido_observacion

# Número de partículas
num_particulas = 100

# Inicialización de partículas
particulas = [random.uniform(0, 1) for _ in range(num_particulas)]

# Inicialización de pesos uniformes
pesos = [1 / num_particulas] * num_particulas

# Datos observados (simulación de mediciones)
observaciones = [3, 4, 5]

# Ciclo principal del filtro de partículas
for observacion_actual in observaciones:
    # Actualizar las partículas
    for i in range(num_particulas):
        particulas[i] = transicion_estado(particulas[i])
        prob_observacion = observacion(particulas[i])
        pesos[i] *= 2.71828 ** (-0.5 * (observacion_actual - prob_observacion) ** 2)
    
    # Normalizar los pesos
    suma_pesos = sum(pesos)
    pesos = [peso / suma_pesos for peso in pesos]
    
    # Resampling (muestreo de partículas)
    indices_resample = random.choices(range(num_particulas), pesos, k=num_particulas)
    particulas = [particulas[i] for i in indices_resample]
    pesos = [1 / num_particulas] * num_particulas

# Estimación del estado final
estado_estimado = sum(particulas) / num_particulas

print("Estado estimado:", estado_estimado)

