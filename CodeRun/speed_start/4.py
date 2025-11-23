n = int(input())
t = [0] * n 
i = 0

while i != n:
    if i == 0 or i == 1:
        t[i] = 1
        i += 1
    else:
        t[i] = t[i - 1] + t[i - 2]
        i += 1

print(sum(t))