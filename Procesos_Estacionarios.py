import random

# Generar una serie temporal simple
serie_temporal = [random.uniform(0, 1) for _ in range(100)]

# Calcular la media y la varianza
media = sum(serie_temporal) / len(serie_temporal)
varianza = sum((x - media) ** 2 for x in serie_temporal) / len(serie_temporal)

print("Serie temporal:", serie_temporal)
print("Media:", media)
print("Varianza:", varianza)

