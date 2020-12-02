import math


def seasons(month):
    if month < 1:
        return 'месяц не найден'
    elif month < 3:
        return 'зима'
    elif month < 6:
        return 'весна'
    elif month < 9:
        return 'лето'
    elif month < 12:
        return 'осень'
    elif month == 12:
        return 'зима'
    else:
        return 'месяц не найден'


def get_month():
    run = True
    while run:
        response = input('Выбери месяц и мы скажем какой это сезон\n')
        if response.lower() == 'выйти':
            break
        try:
            result = seasons(int(response))
            print(result)
        except ValueError:
            print("Введите число")


def is_prime(n):
    if n < 2 or n > 1000:
        return False
    for index in range(2, int(math.sqrt(n)) + 1):
        if (n % index) == 0:
            return False
    return True


# answer = input('Что запустить?\n')
# if answer.lower() == 'месяц':
#     get_month()
# elif answer.lower() == 'число':
# print(is_prime(int(input('Выбери число\n'))))
for number in range(100):
    print(number, is_prime(number))
