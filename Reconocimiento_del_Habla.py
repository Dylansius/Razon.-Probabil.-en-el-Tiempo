#Reconocimiento del Habla

# Mapeo de palabras clave y sus correspondientes comandos
keywords = {
    "hola": "Saludo",
    "adios": "Despedida",
    "reproducir musica": "Reproducir musica",
    "detener musica": "Detener musica"
}

# Función para realizar el reconocimiento del habla simple
def reconocimiento_habla(entrada):
    for palabra, comando in keywords.items():
        if palabra in entrada.lower():
            return comando
    return "Comando no reconocido"

# Grabación de entrada de audio (simulada)
entrada_de_audio = "Hola,puedes reproducir musica, por favor"

# Realizar el reconocimiento del habla
resultado = reconocimiento_habla(entrada_de_audio)

print("Comando reconocido:", resultado)
