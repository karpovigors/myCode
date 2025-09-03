import sys


def main():
    values = list(map(int, sys.stdin.readline().split()))

    values.sort()
    print(values[1])


if __name__ == '__main__':
    main()