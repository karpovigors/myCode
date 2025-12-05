N = int(input())

mas = []
for i in range(N):
    M = int(input())
    M_text = list(map(str, input().split()))
    mas.append(M_text)

i = 0
j = 1
while i < len(mas):
    j = i + 1
    while j < len(mas):
        if set(mas[i]) & set(mas[j]):
            mas[i] = list(set(mas[i] + mas[j]))
            mas.pop(j)
            i = -1
            break
        else:
            j += 1
    i += 1

mas_len = []

for i in range(len(mas)):
    mas_len.append(len(mas[i]))

print(len(mas), max(mas_len))
