
#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
#которые встречаются в обоих наборах. 
#Если таких чисел нет - выдать внятное диагностическое сообщение
#Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

lst1 =  [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
print(lst1)
lst2 = [3, 9, 12, 15, 6, 18]
print(lst2)
print()
lst1 = list(set(lst1))
lst2 = list(set(lst2))
print(lst1)
print(lst2)
lst3 = []
for i in lst1:
    for j in lst2:
        if i == j:
            lst3.append(j)
           
lst3.sort()
print (*lst3)

if len(lst3) == 0: print('Повторяющихся чисел нет')

#решено
