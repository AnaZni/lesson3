lis = input("Введите числа:").split()

for i in range(0, len(lis)-1, 2):
    lis[i], lis[i+1] = lis[i+1], lis[i]

print(lis)