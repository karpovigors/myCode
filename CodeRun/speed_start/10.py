a, b = map(int, input().split())

nod = 0
nok = 0

def nod(a, b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return nod(a - b, b)
    else:
        return nod(a, b - a)

def nok(a, b):
    return a * b / nod(a, b)


print(nod(a, b), int(nok(a, b)))