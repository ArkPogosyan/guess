import random  # Подключаем модуль

# Генерируем случайное число от 1 до 100
number = random.randint(1, 101)


# Функция проверки ввода
def is_valid(user_input):
    if user_input.isdigit():  # Если введено число
        user_input = int(user_input)
        if 1 <= user_input <= 100:  # Проверка диапазона
            return True
        else:
            return False
    else:
        return False



print('Добро пожаловать в числовую угадайку')

# Основной цикл игры
while True:
    response = input('Введите число от 1 до 100: ')

    # Проверяем, является ли введенное значение числом от 1 до 100
    if not is_valid(response):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

    # Преобразуем строку в число
    response = int(response)

    # Сравниваем введённое число с загаданным
    if response < number:
        print('Ваше число меньше загаданного, попробуйте ещё раз.')
    elif response > number:
        print('Ваше число больше загаданного, попробуйте ещё раз.')
    else:
        print('Поздравляю! Вы угадали!')
        break

# Благодарим игрока за игру
print('Спасибо, что играли в числовую угадайку. До новых встреч!')
