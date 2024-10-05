import random

def numAleatorio():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def main():
    num1, num2 = numAleatorio()
    respuesta = input(f'¿Cuánto es {num1} x {num2}? ')
    resultado = num1 * num2

    if int(respuesta) == resultado:
        print('Correcto!')
    else:
        print('Incorrecto')



if __name__ == '__main__':
    main()
