#  Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# lenMSet = int(input('Введите кол-во элементов первого множества: '))
# lenNSet = int(input('Введите кол-во элементов второго множества: '))
# mSet = set()
# nSet = set()
# counterMSet = 0
# while counterMSet < lenMSet:
#     mSet.add(int(input('Введите элемент первого множества: ')))
#     counterMSet += 1
# print()
# counterNSet = 0
# while counterNSet < lenNSet:
#     nSet.add(int(input('Введите элемент второго множества: ')))
#     counterNSet += 1
# print(mSet)
# print(nSet)
# finalSet = nSet.intersection(mSet)
# print(finalSet)



# -------------------------------------------------------------------------------------------
#
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
#
# 4 -> 1 2 3 4
# 9

# shrub = int(input('Введите кол-во кустов: '))
# bushes = list()
# for i in range(1, shrub + 1):
#     bushes.append(i)
# print(bushes)
# maxBerries = 0
# for i in range(len(bushes)):
#     maxBerries = bushes[i - 1] + bushes[i] + bushes[i - 2]
#     i += 1
# print(maxBerries)

