'''
Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на 
экран их сумму, округлённую до трёх знаков после точки.
Пример:
•	Для n = 6 -> 14.072
'''
n = int(input('Enter number: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))


