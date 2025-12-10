import sys


def main():
    text = sys.stdin.read()
    words = text.split()
    print(len(set(words)))


if __name__ == '__main__':
    main()
