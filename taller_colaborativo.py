def recopilar_respuestas(nombre_persona):
    preguntas = [
        "Nombre",
        "Edad",
        "Teléfono",
        "Signo zodiacal",
        "Película favorita",
        "Canción favorita",
        "Comida favorita",
        "¿Cuál es tu lugar soñado para unas vacaciones?",
        "¿Qué habilidad secreta te gustaría tener?",
        "¿Tienes algún talento oculto o pasatiempo inusual?",
        "¿Quién es tu héroe o persona que admiras más y por qué?",
        "¿Cuál es el libro que más te ha impactado y por qué?",
        "¿Si pudieras cenar con cualquier persona, viva o muerta, quién sería y qué le preguntarías?",
        "¿Qué superpoder te gustaría tener y cómo lo usarías?",
        "¿Qué logro personal te enorgullece más hasta ahora?"
    ]
    
    respuestas = {}
    print(f"\nRespuestas de {nombre_persona}:")
    for pregunta in preguntas:
        respuesta = input(f"{pregunta}: ")
        respuestas[pregunta] = respuesta
    
    return respuestas

def mostrar_respuestas(franklin_respuestas, juan_respuestas):
    print("\nRespuestas de Franklin Ramirez:")
    for pregunta, respuesta in franklin_respuestas.items():
        print(f"{pregunta}: {respuesta}")
    
    print("\nRespuestas de Juan Tobar:")
    for pregunta, respuesta in juan_respuestas.items():
        print(f"{pregunta}: {respuesta}")


franklin_respuestas = recopilar_respuestas("Franklin Ramirez")
juan_respuestas = recopilar_respuestas("Juan Tobar")


mostrar_respuestas(franklin_respuestas, juan_respuestas)