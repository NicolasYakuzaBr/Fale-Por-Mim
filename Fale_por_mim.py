import pyttsx3

while True:
# Inicialize o engine
    engine = pyttsx3.init()

# Obtenha todas as vozes disponíveis
    voices = engine.getProperty('voices')

# Encontre a voz do idioma português do Brasil
    for voice in voices:
        if 'brazil' in voice.id:
            engine.setProperty('voice', voice.id)

# Converta o texto em fala
    texto = input('O que você deseja falar?: ')
    engine.say(texto)

# Reproduza a fala
    engine.runAndWait()
    