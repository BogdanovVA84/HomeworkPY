'''
Задача 3 Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
'''
import random
list = [random.randint(0,15) for i in range (25)]
print(list)
new_list =[]
[new_list.append(i) for i in list if i not in new_list ]
print(new_list)


