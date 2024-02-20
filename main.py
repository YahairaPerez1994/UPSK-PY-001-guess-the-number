from random import randint

print("¡Bienvenid@ al juego!")

#Verifica si el numero es el correcto o si es mayor o menor
def check_number(expected_number, actual_number):
    if expected_number == actual_number:
        return "Adivinaste el numero!!"
    elif expected_number > actual_number:
        return "Tu numero es menor que el numero esperado"
    elif expected_number < actual_number:
        return "Tu numero es mayor que el numero esperado"

#Imprime el resultado em pantalla
def print_result(status, player, number = 0):
    if status == "Adivinaste el numero!!" and player == "user":
        print("Usuario ", status)
        return True
    elif status != "Adivinaste el numero!!" and player == "user":
        print(status)
    elif status == "Adivinaste el numero!!" and player == "computer":
        print("La computadora adivino")
        return True
    elif status != "Adivinaste el numero!!" and player == "computer":
        print("La computadora intento: ", number)
    
#Funcion princial
def main_function(expected_number):
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

#Se crear el numero a adivinar
expected_number = randint(1,100)
main_function(expected_number)