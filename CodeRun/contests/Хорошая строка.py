ABC = list("abcdefghijklmnopqrstuvwxyz")
N = int(input())
c = [int(input()) for _ in range(N)]

result = 0
for i in range(0, len(c) - 1):
    result += min(c[i], c[i+1])

print(result)
