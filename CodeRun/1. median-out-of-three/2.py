def main():
    values = list(map(int, input().split()))

    if all(-1000 <= x <= 1000 for x in values):
        values.sort()
        print(values[1])
    else:
        print("Превышение")


if __name__ == '__main__':
    main()