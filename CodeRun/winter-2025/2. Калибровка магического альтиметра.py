def main():
    a = [int(input()) for _ in range(10)]

    def go(i, s):
        if i == 10:
            return s

        # вариант: не берём
        s1 = go(i + 1, s)

        # вариант: берём
        s2 = go(i + 1, s + a[i])

        # выбираем лучший из двух
        d1 = abs(s1 - 100)
        d2 = abs(s2 - 100)

        if d1 < d2:
            return s1
        elif d2 < d1:
            return s2
        else:
            return max(s1, s2)

    print(go(0, 0))

main()
