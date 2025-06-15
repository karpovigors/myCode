def calc(a, b, c):
    try:
        a = float(a)
        c = float(c)

        if b == '+':
            return a + c
        elif b == '-':
            return a - c
        elif b == '*':
            return a * c
        elif b == '/':
            if c == 0:
                return "Ошибка: деление на ноль"
            return a / c
        else:
            return "Ошибка: неверный оператор"
    except ValueError:
        return "Ошибка: введите числа"


a, b, c = input("Введите выражение (например: 5 + 3): ").split()
result = calc(a, b, c)
print(result)