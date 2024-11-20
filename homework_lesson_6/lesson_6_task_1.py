"""
Задание 1. Дан список чисел, отсортированных по возрастанию.
На вход принимается значение, равное одному из элементов списка.
Реализовать функцию, выполняющую рекурсивный алгоритм бинарного поиска,
на выходе программа должна вывести позицию искомого элемента в исходном списке.
"""


def recursive_search(numbers, target, left, right):
    # Находим средний индекс
    middle = (left + right) // 2

    # Если центральный элемент равен числу для поиска, то мы нашли его индекс
    if numbers[middle] == target:
        return middle

    # Если число для поиска меньше центрального, ищем в левой половине и сдвигаем правую границу каждый раз
    elif target < numbers[middle]:
        return recursive_search(numbers, target, left, middle - 1)

    # Иначе ищем в правой половине и сдвигаем левую границу
    else:
        return recursive_search(numbers, target, middle + 1, right)


# Задаем список чисел
numbers = [1, 3, 5, 7, 9, 11, 13, 15]

# Вводим число для поиска
target = int(input("Введите число для поиска: "))

# Вызов функции
result = recursive_search(numbers, target, 0, len(numbers) - 1)

# Выводим результат
if result != -1:
    print(f"Искомое число {target} находится на позиции {result + 1}.")  # +1, чтобы нумерация была с 1
else:
    print(f"Число {target} не найдено в списке.")
