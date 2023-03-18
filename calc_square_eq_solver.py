from math import sqrt
from typing import Union


def square_eq_solver(a: Union[int, float],
                     b: Union[int, float],
                     c: Union[int, float]) -> list[Union[int, float]]:
    """Вычисляет корни квадратного уравнения вида Ах2 + Вх + С."""
    result = []
    discriminant = b * b - 4 * a * c

    if discriminant == 0:
        result.append(-b / (2 * a))
    elif discriminant > 0:
        result.append((-b + sqrt(discriminant)) / (2 * a))
        result.append((-b - sqrt(discriminant)) / (2 * a))

    return result


def show_result(data):
    if len(data) > 0:
        for index, value in enumerate(data):
            print(f'Корень номер {index + 1} равен {value:.02f}')
    else:
        print('Уравнение с заданными параметрами не имеет корней')


def main():
    a, b, c = map(int,
                  input('Пожалуйста, введите три числа через пробел: ').split())
    result = square_eq_solver(a, b, c)
    show_result(result)


if __name__ == '__main__':
    main()
