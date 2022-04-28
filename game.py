from random import randint
#Variables
vida_pikachu = 80
vida_pokemon = 90

print("Juego de Pokemon")
nombre_jugador = input("¿Que nombre le quieres dar a tu Pokemon?\n")


while vida_pikachu > 0 and vida_pokemon > 0:

    print("¡¡¡¡¡¡¡Turno de Pikachu!!!!!")
    ataque_pikachu = randint(1,3)
    if ataque_pikachu == 1:
        print("Pikachu usa Voltio !!!!")
        vida_pokemon -= 10
    elif ataque_pikachu == 2:
        print("Pikachu se cura")
        vida_pikachu += 10
    elif ataque_pikachu == 3:
        print("Pikachu usa Placaje!!!!")
        vida_pokemon -= 5

    print("La vida de {} es de : {}, y la vida de Pikachu es de {}".format(nombre_jugador,vida_pokemon,vida_pikachu))
    input("Presione cualquier tecla para continuar ..")
    print("Turno de {}".format(nombre_jugador))

    ataque_pokemon = None
    while  ataque_pokemon != "P" and ataque_pokemon != "A" and ataque_pokemon != "B" and ataque_pokemon != "p" and ataque_pokemon != "a" and ataque_pokemon != "b":
     ataque_pokemon = input("¿Que ataque deseas realizar?\n "
                               "[P] Placaje \n"
                               " [A] Agua \n"
                               " [B] Burbuja\n")
    if ataque_pokemon == "P" or ataque_pokemon =="p":
        print("{} Usa Placajae !!!!".format(nombre_jugador))
        vida_pikachu -= 2
    elif ataque_pokemon == "A" or ataque_pokemon == "a":
        print("{} Usa Pistola de Agua !!!!".format(nombre_jugador))
        vida_pikachu -= 10
    elif ataque_pokemon == "B" or ataque_pokemon == "b":
        print("{} Usa Burbuja !!!!".format(nombre_jugador))
        vida_pikachu -= 5

    print("La vida de {} es de: {}, y la vida de Pikachu es de {}".format(nombre_jugador,vida_pokemon,vida_pikachu))
    input("Presione cualquier tecla para continuar ..")


if vida_pokemon > vida_pikachu:
    print("Pikachu es el ganador")
else:
    print("{} Es el ganador".format(nombre_jugador))