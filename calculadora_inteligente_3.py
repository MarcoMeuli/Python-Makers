import random

def numAleatorio():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2


def preguntarOperador():
    ope = input('\nQue operacion quieres hacer? (+, -, *, /): ')
    while not ope in ['+', '-', '*', '/']:
        print('Introduce un operador correcto (+, -, *, /)')
        ope = input('\nQue operacion quieres hacer? (+, -, *, /): ')
    return ope


def main():
    print('--> CALCULADORA INTELIGENTE 3 <--\n')

    ope = preguntarOperador()
    num1, num2 = numAleatorio()

    if ope == '+':
        respuesta = input(f'¿Cuánto es {num1} + {num2}? ')
        resultado = num1 + num2
    elif ope == '-':
        respuesta = input(f'¿Cuánto es {num1} - {num2}? ')
        resultado = num1 - num2
    elif ope == '*':
        respuesta = input(f'¿Cuánto es {num1} * {num2}? ')
        resultado = num1 * num2
    elif ope == '/':
        respuesta = input(f'¿Cuánto es {num1} / {num2}? ')
        resultado = num1 / num2


    if int(respuesta) == resultado:
        print('Correcto!')
    else:
        print('Incorrecto')




if __name__ == '__main__':
    main()


