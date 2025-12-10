import sys


def main():

    counter = {}

    for line in sys.stdin:
        for word in line.split():
            print(counter.get(word, 0), end=' ')
            counter[word] = counter.get(word, 0) + 1


if __name__ == '__main__':
    main()
