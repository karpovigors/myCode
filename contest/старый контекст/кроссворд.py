R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

def filter_func(line):
    return [word for word in line.split("#") if len(word) >= 2]

mas = []

for row in crossword:
    mas.extend(filter_func(row))

for col in range(C):
    columns = "".join(crossword[row][col] for row in range(R))
    mas.extend(filter_func(columns))

print(min(mas))