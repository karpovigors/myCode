import sys

result = {}

for line in sys.stdin:
    person, item, amount = line.split()
    amount = int(amount)

    if person not in result:
        result[person] = {}

    result[person][item] = result[person].get(item, 0) + amount

for person in sorted(result):
    print(f"{person}:")
    for item in sorted(result[person]):
        print(item, result[person][item])