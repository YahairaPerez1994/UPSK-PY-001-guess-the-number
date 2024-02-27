# Importe la función randint del modulo random
from random import randint

# Función para verificar si el número adivinado es correcto o no
def check_number(expected_number, actual_number):
    if expected_number == actual_number:
        return "Adivinaste el numero!!"
    elif expected_number > actual_number:
        return "El número esperado es mayor que el número que has ingresado"
    elif expected_number < actual_number:
        return "El número esperado es menor que el número que has ingresado"

# Función para imprimir el resultado en pantalla
def print_result(status, player, number = 0):
    if status == "Adivinaste el numero!!" and player == "user":
        print("¡Felicidades! Has adivinado el número correcto")
        return True
    elif status != "Adivinaste el numero!!" and player == "user":
        print(status)
    elif status == "Adivinaste el numero!!" and player == "computer":
        print("La computadora adivino")
        return True
    elif status != "Adivinaste el numero!!" and player == "computer":
        print("La computadora intento:", number)
    
#Funcion princial
def main_function(expected_number):
    print("¡Bienvenid@ al juego de Adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    while True:
        user_number = int(input("Ingresa un numero entre 1 y 100: "))
        status = check_number(expected_number, user_number)
        result = print_result(status, 'user')
        if result:
            break

        computer_number = randint(1,100)
        status = check_number(expected_number, computer_number)
        result = print_result(status, 'computer', computer_number)
        if result:
            break

# Código para llamar a la función main_function con un número aleatorio
if __name__ == '__main__':
  expected_number = randint(1,100)  # Genera un número aleatorio que el jugador debe adivinar
  main_function(expected_number)   # Llama a la función principal del juego
