# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

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
	node = 0
	while index < len(text):
		if text[index] in trie[node]:
			node = trie[node][text[index]]
			if trie[node] == {}:
				return True
			index += 1
		else:
			return False



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
    return tree

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range(n):
	patterns += [sys.stdin.readline ().strip ()]

'''
text = input("Text: ")
n = int(input("n: "))
for _ in range(n):
	patterns.append(input("Pattern: "))
'''
ans = solve (text, n, patterns)

#print(ans)
sys.stdout.write (' '.join (map (str, ans)) + '\n')
