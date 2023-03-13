#Uses python3

import sys
import random
import time

def dfs(adj, x=0):
    #write your code here
    global visited,order
    visited[x] = True
    for neighbor in adj[x]:
        if visited[neighbor] == False:
            dfs(adj,neighbor)
    order.append(x)

def toposort(adj):
    global visited,order
    order = []
    visited = [False] * len(adj)
    '''
    # Intuitive solution but makes runtime O(n^2) due to searching entire array
    # for False index each time it chooses a new node

    while True:
        try:
            dfs(adj,visited.index(False))
        except:
            break
        '''
    for ind in range(len(adj)):
        if visited[ind] == False:
            dfs(adj,ind)
        

    #order.reverse()
    return order


if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    '''
    
    n,m = 100000,100000
    edges = []
    for _ in range(100000):
        x = random.randrange(1,100000)
        y = random.randrange(1,100000)
        edges.append((x,y))
        
    ti = time.time()
    '''
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)

    #for x in order:
     #   print(x + 1, end=' ')

    for ind in range(len(order)):
        print(order[-(ind+1)]+1,end=" ")