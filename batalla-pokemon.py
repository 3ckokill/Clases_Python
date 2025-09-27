import random


class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre


class Pokemon:
    def __init__(self, nombre, ataque_max, vida_max):
        self.nombre = nombre
        self.ataque_max = ataque_max
        self.vida_max = vida_max
        self.vida_actual = vida_max

    def mostrar_estadisticas(self):
        print(
            f"Pokémon: {self.nombre} | Ataque máximo: {self.ataque_max} | Vida máxima: {self.vida_max} | Vida actual: {self.vida_actual}")


mi_entrenador = None
mi_pokemon = None
rival_entrenador = None
rival_pokemon = None


def crearEntrenadorPokemon(num):
    global mi_entrenador, mi_pokemon, rival_entrenador, rival_pokemon
    nombre_ent = input("Ingrese el nombre del entrenador: ").strip()
    if not nombre_ent:
        nombre_ent = "Entrenador" + str(num)
    nombre_pok = input("Ingrese el nombre del pokemon: ").strip()
    if not nombre_pok:
        nombre_pok = "Pokemon" + str(num)
    ataque = random.randint(20, 100)
    vida = random.randint(150, 400)
    if num == 1:
        mi_entrenador = Entrenador(nombre_ent)
        mi_pokemon = Pokemon(nombre_pok, ataque, vida)
        print("\n--- Su entrenador y Pokémon creados ---")
        print(f"Entrenador: {mi_entrenador.nombre}")
        mi_pokemon.mostrar_estadisticas()
    else:
        rival_entrenador = Entrenador(nombre_ent)
        rival_pokemon = Pokemon(nombre_pok, ataque, vida)
        print("\n--- Rival creado ---")
        print(f"Entrenador: {rival_entrenador.nombre}")
        rival_pokemon.mostrar_estadisticas()


def valorDeAtaque(num):
    if num == 1:
        return random.randint(0, mi_pokemon.ataque_max)
    else:
        return random.randint(0, rival_pokemon.ataque_max)


def defender(num, valor_ataque):
    dado = random.randint(1, 6)
    if dado == 6:
        valor_ataque = 0
        print("¡Tirada del dado = 6! Ataque anulado (0 daño).")
    if num == 1:
        mi_pokemon.vida_actual -= valor_ataque
        if mi_pokemon.vida_actual < 0:
            mi_pokemon.vida_actual = 0
        return mi_pokemon.vida_actual
    else:
        rival_pokemon.vida_actual -= valor_ataque
        if rival_pokemon.vida_actual < 0:
            rival_pokemon.vida_actual = 0
        return rival_pokemon.vida_actual


def recuperar():
    mi_pokemon.vida_actual = mi_pokemon.vida_max


def main():
    print(" Examen: Pelea Pokémon ")
    crearEntrenadorPokemon(1)
    victorias = 0
    derrotas = 0
    while True:
        opcion = input(
            "\nElija opción: [P]elear  -  [F]inalizar: ").strip().upper()
        if opcion == "P":
            crearEntrenadorPokemon(2)
            recuperar()
            print("\n Comienza la pelea! ")
            print("Estado inicial:")
            print(f"{mi_entrenador.nombre}: ", end="")
            mi_pokemon.mostrar_estadisticas()
            print(f"{rival_entrenador.nombre}: ", end="")
            rival_pokemon.mostrar_estadisticas()
            turno = 1
            while True:
                if turno == 1:
                    ataque = valorDeAtaque(1)
                    print(
                        f"\n{mi_entrenador.nombre} ({mi_pokemon.nombre}) ataca con fuerza {ataque}.")
                    vida_rival = defender(2, ataque)
                    print(
                        f"Resumen: {rival_entrenador.nombre} - {rival_pokemon.nombre} -> vida actual = {vida_rival}")
                    if vida_rival <= 0:
                        print(
                            f"\n¡Victoria! {mi_entrenador.nombre} con {mi_pokemon.nombre} GANÓ la pelea.")
                        victorias += 1
                        break
                    turno = 2
                else:
                    ataque = valorDeAtaque(2)
                    print(
                        f"\n{rival_entrenador.nombre} ({rival_pokemon.nombre}) ataca con fuerza {ataque}.")
                    vida_mia = defender(1, ataque)
                    print(
                        f"Resumen: {mi_entrenador.nombre} - {mi_pokemon.nombre} -> vida actual = {vida_mia}")
                    if vida_mia <= 0:
                        print(
                            f"\n¡Derrota! {rival_entrenador.nombre} con {rival_pokemon.nombre} GANÓ la pelea.")
                        derrotas += 1
                        break
                    turno = 1
        elif opcion == "F":
            print("\n--- Finalizando el juego ---")
            print("Sus datos finales:")
            print(f"Entrenador: {mi_entrenador.nombre}")
            mi_pokemon.mostrar_estadisticas()
            print(f"Encuentros ganados: {victorias}")
            print(f"Encuentros perdidos: {derrotas}")
            print("Gracias por jugar. Fin.")
            break
        else:
            print("Opción no válida. Ingrese 'P' para pelear o 'F' para finalizar.")


if __name__ == "__main__":
    main()
