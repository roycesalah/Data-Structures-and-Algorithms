# python3
import sys

NA = -1

class Node:
    def __init__ (self):
        self.next = [NA] * 4
        self.patternEnd = False

def solve (text, n, patterns):
    result = []
    trie = build_trie(patterns)
    index = 0
    while index < len(text):
        if trie_match(text,trie,index):
            result.append(index)
        index += 1

    return result

def trie_match(text,trie,index):
    node = trie
    while index < len(text):
        if node.next[let2ind(text[index])] != NA:
            node = node.next[let2ind(text[index])]
            if node.patternEnd == True:
                return True
            index += 1
        else:
            return False


'''
def build_trie(patterns):
    tree = dict({0:{}})
    node_num = 1
    for pattern in patterns:
        current_node = 0
        for char in pattern:
            if char in tree[current_node]:
                current_node = tree[current_node][char]
            else:
                tree[current_node].update({char:node_num})
                tree.update({node_num:{}})
                current_node = node_num
                node_num += 1
    return tree'''

def let2ind(letter):
    return ["A","C","G","T"].index(letter)

def build_trie(patterns):
    trie = Node()
    for pattern in patterns:
        current_node = trie
        for ind in range(len(pattern)):
            next_ind = let2ind(pattern[ind])
            if current_node.patternEnd == True:
                break
            elif current_node.next[next_ind] != NA:
                current_node = current_node.next[next_ind]
                if ind == len(pattern)-1:
                    current_node.patternEnd = True
            else:
                next_node = Node()
                if ind == len(pattern)-1:
                    next_node.patternEnd = True
                current_node.next[next_ind] = next_node
                current_node = next_node
    return trie

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

'''
text = input("Text: ")
n = int(input("n: "))
for _ in range(n):
	patterns.append(input("Pattern: "))
'''

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')

#print(ans)