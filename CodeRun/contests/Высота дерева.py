import sys


def main():
    def add(root, x):
        if root is None:
            return [x, None, None]
        if x < root[0]:
            root[1] = add(root[1], x)
        elif x > root[0]:
            root[2] = add(root[2], x)
        return root

    def height(root):
        if root is None:
            return 0
        return 1 + max(height(root[1]), height(root[2]))

    root = None

    for x in map(int, input().split()):
        if x == 0:
            break
        root = add(root, x)

    print(height(root))



if __name__ == '__main__':
    main()
