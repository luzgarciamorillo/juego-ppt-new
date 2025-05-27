# -------------------------------------------------------
# Juego de Piedra, Papel o Tijera
# -------------------------------------------------------
jugador1 = input("¡Hola Jugador 1! ¿Qué eliges? ¿Piedra, Papel o Tijera?: ")
jugador2 = input("¡Hola Jugador 2! ¿Qué eliges? ¿Piedra, Papel o Tijera?: ")

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Papel" and jugador2 == "Piedra") or (jugador1 == "Tijera" and jugador2 == "Papel"):
    print("¡Jugador 1 ha ganado!")
else:
    print("¡Jugador 2 ha ganado!")

# Podemos complejizarlo
nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

jugador1 = input("¡Hola jugador 1! ¿Qué eliges? ¿Piedra, Papel o Tijera?: ")
jugador2 = input("¡Hola jugador 2! ¿Qué eliges? ¿Piedra, Papel o Tijera?: ")

condicion1 = jugador1 == "Piedra" and jugador2 == "Tijera"
condicion2 = jugador1 == "Papel" and jugador2 == "Piedra"
condicion3 = jugador1 == "Tijera" and jugador2 == "Papel"

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado:", nombre1)
else:
    print("Ha ganado:", nombre2)
# Refactorización: reescribir el código para que sea más legible y reutilizable.