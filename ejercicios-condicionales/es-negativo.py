while True:
    try:
        nota = float(input('Introduce un numero: '))

        if nota > 0:
            print('Introduce un numero negativo.')
            nota = float(input('\nIntroduce un numero: '))
        else:
            break

    except ValueError:
        print('Error: Introduce un numero.\n')
print('Correcto')
