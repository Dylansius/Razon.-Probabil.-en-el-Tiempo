import random

# Funci�n de transici�n de estado
def transicion_estado(estado_anterior):
    # Simulaci�n de movimiento del objeto
    ruido_transicion = random.gauss(0, 0.1)  # Ruido de la transici�n
    nuevo_estado = estado_anterior + 1 + ruido_transicion
    return nuevo_estado

# Funci�n de observaci�n
def observacion(estado):
    # Simulaci�n de medici�n
    ruido_observacion = random.gauss(0, 1)  # Ruido de la observaci�n
    return estado + ruido_observacion

# N�mero de part�culas
num_particulas = 100

# Inicializaci�n de part�culas
particulas = [random.uniform(0, 1) for _ in range(num_particulas)]

# Inicializaci�n de pesos uniformes
pesos = [1 / num_particulas] * num_particulas

# Datos observados (simulaci�n de mediciones)
observaciones = [3, 4, 5]

# Ciclo principal del filtro de part�culas
for observacion_actual in observaciones:
    # Actualizar las part�culas
    for i in range(num_particulas):
        particulas[i] = transicion_estado(particulas[i])
        prob_observacion = observacion(particulas[i])
        pesos[i] *= 2.71828 ** (-0.5 * (observacion_actual - prob_observacion) ** 2)
    
    # Normalizar los pesos
    suma_pesos = sum(pesos)
    pesos = [peso / suma_pesos for peso in pesos]
    
    # Resampling (muestreo de part�culas)
    indices_resample = random.choices(range(num_particulas), pesos, k=num_particulas)
    particulas = [particulas[i] for i in indices_resample]
    pesos = [1 / num_particulas] * num_particulas

# Estimaci�n del estado final
estado_estimado = sum(particulas) / num_particulas

print("Estado estimado:", estado_estimado)

