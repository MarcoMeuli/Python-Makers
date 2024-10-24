nums = []
nums_par = []

for i in range(101):
    nums.append(i)


for num in nums:
    if num % 2 == 0:
        nums_par.append(num)


print('Lista normal:', nums)
print('\nLista de pares:', nums_par)