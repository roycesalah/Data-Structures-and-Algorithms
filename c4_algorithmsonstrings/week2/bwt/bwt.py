# python3
import sys

def BWT(text):
    rotations = []
    transform = ""
    for _ in range(len(text)):
        char0 = text[0]
        text = text.replace(text[0],"",1) + char0
        rotations.append(text)
    rotations.sort()
    for rotation in rotations:
        transform += rotation[-1]
    return transform

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))