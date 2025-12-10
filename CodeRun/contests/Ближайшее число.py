import sys


def main():
    N = int(input())
    mas = list(map(int, input().split()))
    F = int(input())

    min_mas = float('inf')
    raznitsa = 0

    for num in mas:
        mas_abs = abs(num - F)

        if mas_abs < min_mas:
            min_mas = mas_abs
            raznitsa = num

    print(raznitsa)



if __name__ == '__main__':
    main()
