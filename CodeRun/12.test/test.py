import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    N = int(input())

    comp = [[] for _ in range(N)]
    for _ in range(N):
        N = map(int, input().split())
        comp[N].append(N)


    print("Hello")



if __name__ == '__main__':
    main()
