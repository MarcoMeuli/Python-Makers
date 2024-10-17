nota = int(input(': '))

if nota < 0 or nota > 100:
    print('Esa nota es incorrecta')

elif nota < 50:
    print('Suspenso')
elif nota >= 50 and nota < 70:
    print('Bien')
elif nota >= 70 and nota < 90:
    print('Notable')
elif nota >= 90:
    print('Sobresaliente')
