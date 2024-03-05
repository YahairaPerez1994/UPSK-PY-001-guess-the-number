from random import randint
from game_logic import *

#Funcion princial
def main_function(expected_number):
    user_guesses = []  # Lista para almacenar los números intentados por el usuario.
    computer_guesses = []  # Lista para almacenar los números intentados por la computadora.
    print("¡Bienvenid@ al juego de Adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?\n")
    a = 1  # Límite inferior del rango de números posibles.
    b = 100   # Límite superior del rango de números posibles.
    while True:#bucle deljuego
        print("----------------USUARIO-------------------\n")
        user_number = int(input("Ingresa un numero entre 1 y 100: ")) #Solicita al usuario que ingrese un número
        user_guesses.append(user_number)  # Se agrega el número a la lista de intentos del usuario.
        status = check_number(expected_number, user_number) #Se comprueba si el número es correcto.
        print_result(status, 'user') #impresión del resultado del usuario
        print("------------------------------------------\n")
        if status == "igual":   # Si el número es correcto, el usuario gana y el juego termina.
            print("Tus suposiciones fueron:", user_guesses)
            break

        if len(computer_guesses) == 0:  # La primera vez, la computadora hace un intento aleatorio.
            computer_number, a, b = computer_function(a, b)
        else:  # Después, la computadora utiliza una estrategia basada en el resultado del intento anterior.
            computer_number, a, b = computer_function(a, b, computer_number, status_computer)
        computer_guesses.append(computer_number)
        status_computer = check_number(expected_number, computer_number) # Se comprueba si el número de la computadora es correcto.
        print("-------------COMPUTADORA------------------\n")
        print_result(status_computer, 'computer', computer_number)
        print("------------------------------------------\n")
        if status_computer == "igual": # Si el número de la computadora es correcto, la computadora gana y el juego termina.
            print("Las suposiciones de la computadora fueron:", computer_guesses)
            break


if __name__ == '__main__':
    expected_number = randint(1, 100)  # Se genera un número aleatorio para que el usuario lo adivine.
    main_function(expected_number)  # Se inicia el juego con el número generado.
