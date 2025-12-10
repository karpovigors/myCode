import sys


def main():
    n = list(map(int, input().split()))
    n.sort(reverse=True)
    minus = [mas for mas in n if mas < 0]
    minus.sort()

    if len(minus) >= 2:
        if (minus[0] * minus[1] * n[0]) > (n[0] * n[1] * n[2]):
            if (minus[0] * minus[1]) > n[0]:
                print(minus[0], minus[1], n[0])
            elif (minus[0] * minus[1]) > n[1]:
                print(n[0], minus[0], minus[1])
            else:
                print(*n[:3])
        else:
            print(*n[:3])
    else:
        print(*n[:3])


if __name__ == '__main__':
    main()
