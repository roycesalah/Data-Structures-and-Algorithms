# python3

import sys
import threading


def compute_height(n, parents):
    # Construct empty array for nodes [[children],height]
    tree = []
    for _ in range(n):
        tree.append([[],1])

    for i in range(n):        
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]][0].append(i)

    queue = [tree[root]]
    max_height = 0 
    while queue != []:
        if queue[0][1] > max_height:
            max_height = queue[0][1]
        for child in queue[0][0]:
            tree[child][1] = queue[0][1] + 1
            queue.append(tree[child])
        queue.pop(0)

    return max_height




def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
