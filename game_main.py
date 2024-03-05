from random import randint
from game_logic import *

#Funcion princial
def main_function(expected_number):
    user_guesses = []
    computer_guesses = []
    print("¡Bienvenid@ al juego de Adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    a = 1
    b = 100
    while True:#bucle deljuego
        print("----------------USUARIO-------------------")
        user_number = int(input("Ingresa un numero entre 1 y 100: ")) #Solicita al usuario que ingrese un número
        user_guesses.append(user_number)
        status = check_number(expected_number, user_number) #verificación del usuario
        print_result(status, 'user') #impresión del resultado del usuario
        print("------------------------------------------")
        if status == "igual": 
            print("Tus suposiciones fueron:", user_guesses)
            break #Si el usuario adivina correctamente el número, el juego termina y el bucle se rompe con la instrucción break.

        if len(computer_guesses) == 0:
            computer_number, a, b = computer_function(a, b)
        else:
            computer_number, a, b = computer_function(a, b, computer_number, status_computer)
        computer_guesses.append(computer_number)
        status_computer = check_number(expected_number, computer_number)
        print("-------------COMPUTADORA------------------")
        print_result(status_computer, 'computer', computer_number)
        print("------------------------------------------")
        if status_computer == "igual":
            print("Las suposiciones de la computadora fueron:", computer_guesses)
            break


if __name__ == '__main__':
    expected_number = randint(1, 100)  # Se genera un número aleatorio para que el usuario lo adivine.
    main_function(expected_number)  # Se inicia el juego con el número generado.
