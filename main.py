lis = input("Введите числа:").split()

for i in range(0, len(lis)-1, 2):
    lis[i], lis[i+1] = lis[i+1], lis[i]

print(lis)


***************
number =int(input("Введите номер месяца: \n> "))
months={1:'Январь',2:'Февраль',3:'Март',4:'Апрель',5:'Май',6:'Июнь',7:'Июль',8:'Август',9:'Сентябрь',10:'Октябрь',11:'Ноябрь',12:'Декабрь'}
if number<13:
    print(months[number])
else:print("Такого месяца нет")
    
    
**************
while True:
    str = input('ВВедите слова: ')
    if len(str) < 3 or str.count(' ') < 1:
        print('Попробуйте еще раз')
        continue

    break

for index, word in enumerate(str.split()):
    print(index + 1, (word, word[:10])[len(word) > 10])
