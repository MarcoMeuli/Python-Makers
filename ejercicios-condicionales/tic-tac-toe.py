import random

def jugadas():
    opciones = ['piedra', 'papel', 'tijeras']
    j1 = input('¿Piedra papel o tijeras?: ').lowe()
    j2 = random.choice(opciones)

    return (j1, j2)

def ganador(j1, j2):
    match (j1, j2):
        case ('piedra', 'tijeras'):
            print('Gana el jugador.')
        case ('papel', 'piedra'):
            print('Gana el jugador.')
        case ('tijeras', 'papel'):
            print('Gana el jugador.')

        case ('tijeras', 'piedra'):
            print('Gana el ordenador.')
        case ('piedra', 'papel'):
            print('Gana el ordenador.')
        case ('papel', 'tijeras'):
            print('Gana el ordenador.')


        case _:
            print('Empate.')

def main():
    j1, j2 = jugadas()
    ganador()

main()