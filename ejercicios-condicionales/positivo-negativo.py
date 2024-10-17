while True:
    while True:
        try:
            num = int(input(': '))
            break
        except ValueError:
            print(f'Esto no es un numero')

    if num > 0:
        print(f'{num} es positivo.')
    elif num < 0:
        print(f'{num} es negativo.')
    else:
        print(f'Este numero es 0')
