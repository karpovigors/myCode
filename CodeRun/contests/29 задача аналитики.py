import sys
import math

def main():
    a, b, c = map(int, input().split())

    D = (b**2) - (4 * a * c)

    if D == 0:
        x = -b / (2 * a)
        print(1)
        print(x)
    elif D > 0:
        x_minus = (-b - math.sqrt(D)) / (2 * a)
        x_plus = (-b + math.sqrt(D)) / (2 * a)
        print(2)
        print(x_minus, x_plus)
    elif D < 0:
        print(0)


if __name__ == '__main__':
    main()
