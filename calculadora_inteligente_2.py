import random

def numAleatorio():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def main():
    NUM_REPS = 5
    aciertos = 0
    for i in range(NUM_REPS):
        num1, num2 = numAleatorio()
        respuesta = input(f'Pregunta{i+1}. ¿Cuánto es {num1} x {num2}?: ')
        resultado = num1 * num2

        if int(respuesta) == resultado:
            aciertos += 1

    print(f'\nHas tenido {aciertos} aciertos.')



if __name__ == '__main__':
    print('--> CALCULADORA INTELIGENTE 2 <--\n')
    main()
