# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i+1,next))

        if next in ")]}":
            popped = False
            if opening_brackets_stack == []:
                pass
            elif are_matching(opening_brackets_stack[-1][1],next):
                opening_brackets_stack.pop(-1)
                popped = True
            if popped == False:
                return i+1
            
            
    if len(opening_brackets_stack) == 0:
        return "Success"
    return opening_brackets_stack[0][0]


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
