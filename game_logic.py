from random import randint

#Función para verificar si el número ingresado coincide con el número esperado.
def check_number(expected_number, actual_number):
    if expected_number == actual_number:
        return "igual"
    elif expected_number > actual_number:
        return "menor"
    elif expected_number < actual_number:
        return "mayor"


# Imprime el resultado del juego para el jugador y, en caso de ser necesario, el número intentado por la computadora.
def print_result(status, player, number = 0):
    if status == "igual":
        if player == "user":
            print("¡Felicidades! usuario has adivinado el número correcto.")
        else:  # player == "computer"
            print(f"La computadora intento: {number}\nLa computadora adivinó el número correcto")
    else:
        if player == 'computer':
            print(f"La computadora intentó: {number}, pero no adivinó correctamente.")

        if status == "menor":
            print("El número esperado es mayor que el número ingresado.")  # Imprime si el número esperado es mayor/menor
        elif status == "mayor":
            print("El número esperado es menor que el número ingresado.")


# Calcula el próximo intento de la computadora en función del resultado del intento anterior.
def computer_function(a, b, computer_number = 0, status = 0):
    if status == 'menor':
        a = computer_number + 1
        return randint(a, b), a, b
    elif status == 'mayor':
        b = computer_number - 1
        return randint(a, b), a, b
    else:
        return randint(a, b), a, b
