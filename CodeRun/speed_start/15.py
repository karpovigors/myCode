mas = []
i = 0
while i == 0:
    n = int(input())
    if n == (-2 * 10**9):
        break
    else:
        mas.append(n)

j = 0
while j != len(mas) - 1:
    if len(set(mas)) == 1:
        j+=1
        status = "CONSTANT"
    elif mas == sorted(mas) and len(set(mas)) == len(mas):
        j+=1
        status = "ASCENDING"
        break
    elif sorted(mas) == mas:
        j+=1
        status = "WEAKLY ASCENDING"
    elif mas == sorted(mas, reverse=True) and len(set(mas)) == len(mas):
        j+=1
        status = "DESCENDING"
    elif sorted(mas, reverse=True) == mas:
        j+=1
        status = "WEAKLY DESCENDING"
    else:
        j+=1
        status = "RANDOM"

print(status)