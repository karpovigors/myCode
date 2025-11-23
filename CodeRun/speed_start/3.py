list_sosedi = list(map(int, input().split()))
i = 1
k = 0
while i < len(list_sosedi):
    if i == len(list_sosedi) - 1:
        break
    if list_sosedi[i-1] < list_sosedi[i] > list_sosedi[i+1]:
        k += 1
        i += 1
    else:
        i += 1
print(k)