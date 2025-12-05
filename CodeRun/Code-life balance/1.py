N = int(input())
mas=[int(input()) for _ in range(N)]
j = [[0] for _ in range(N)]
for i in range(len(mas)):
    if mas[i] > 100:
        j += 1