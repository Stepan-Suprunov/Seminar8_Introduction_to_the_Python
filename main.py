# Работа с записью в файл

import time

with open('test20.txt', 'r', encoding='utf-8') as file:
find_letter = input()
count = 0
for letter in file.read():
if letter == find_letter:
count += 1
print(count)


with open('test20.txt', 'r', encoding='utf-8') as file:
find_letter = input()
print(file.read().count(find_letter))


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
n = int(input('Введите кол-во элементов в списке: '))
some_list = [randint(-n, n) for _ in range(n)]
print(some_list)
with open('les8test.txt', 'w', encoding='utf-8') as file:
    for _ in range(randint(1, n)):
        file.write(str(randint(0, n - 1)) + '\n')

with open('les8test.txt', 'r', encoding='utf-8') as file:
    mult = 1
    for ind in file.read().splitlines():
        mult *= some_list[int(ind)]
print(mult)
