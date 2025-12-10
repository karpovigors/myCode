import sys


def main():
    mas = list(map(int, input().split()))
    mas.sort()
    if (mas[0] * mas[1]) > (mas[-1] * mas[-2]):
        print(*mas[0:2])
    else:
        print(*mas[-2:])


if __name__ == '__main__':
    main()
