first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third: # у меня программа такое условие считала и не вывела ошибку, но я не уверена, что это условие написано корректно. Поправьте меня, если я неправа)
#if first == second and second == third: - такая запись условия if будет более корректной?
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print (0)