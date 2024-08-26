import getpass

def obtener_jugada(jugador):
    jugada = getpass.getpass(f"{jugador}, elige piedra, papel o tijera (tu elección no se mostrará): ").lower()
    while jugada not in ["piedra", "papel", "tijera"]:
        print("Opción inválida. Por favor elige piedra, papel o tijera.")
        jugada = getpass.getpass(f"{jugador}, elige piedra, papel o tijera: ").lower()
    return jugada

def determinar_ganador(jugada1, jugada2, jugador1, jugador2):
    if jugada1 == jugada2:
        return "Empate"
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
         (jugada1 == "papel" and jugada2 == "piedra") or \
         (jugada1 == "tijera" and jugada2 == "papel"):
        return f"{jugador1} gana"
    else:
        return f"{jugador2} gana"

# Juego principal
jugador1 = input("Nombre del Jugador 1: ")
jugador2 = input("Nombre del Jugador 2: ")

while True:
    jugada1 = obtener_jugada(jugador1)
    jugada2 = obtener_jugada(jugador2)

    resultado = determinar_ganador(jugada1, jugada2, jugador1, jugador2)
    
    print(f"\n{jugador1} eligió: {jugada1}")
    print(f"{jugador2} eligió: {jugada2}")
    
    if resultado == "Empate":
        print("¡Empate! Los jugadores deben volver a jugar.\n")
    else:
        print(f"\n{resultado}")
        break
