import sys


def main():
    s = input()
    stack = []

    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                print("no")
                break
    else:
        print("yes" if not stack else "no")



if __name__ == '__main__':
    main()
