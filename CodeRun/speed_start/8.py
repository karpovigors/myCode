N = list(map(int, input().split()))
i = 1
t = "YES"
while i < len(N):
    if N[i-1] >= N[i]:
        t = "NO"
        break
    else:
        i += 1
print(t)