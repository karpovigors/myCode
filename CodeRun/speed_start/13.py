N = int(input())
mas = list(map(int, input().split()))

i = 0

if mas == mas[::-1]:
    print(0)
while mas != mas[::-1]:
    mas_res = []
    mas_rest = []
    mas_res = mas[0:i:]
    mas_rest = mas + mas_res[::-1]
    if mas_rest == mas_rest[::-1]:
        print(len(mas_res))
        print(*mas_res[::-1])
        break
    else:
        i+= 1