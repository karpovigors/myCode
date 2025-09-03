def main():
    # Ввод, N - количество вершин, M - количество ребер
    N, M = map(int, input().split())

    # Лучший вариант решения задачи - список смежности для графа
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)  # граф неориентированный

    # Для гарантии уникальности
    visited = set()

    # Стек для итеративного dfs, начиная с вершины 1
    stack = [1]

    #Итеративный DFS
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    # Сортировка по возрастанию для окончательного вывода
    result = sorted(visited)
    print(len(result))
    print(*result)


if __name__ == '__main__':
    main()
