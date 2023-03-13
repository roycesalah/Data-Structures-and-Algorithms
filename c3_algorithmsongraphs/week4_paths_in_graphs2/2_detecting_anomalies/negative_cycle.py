#Uses python3

import sys
from math import inf
from queue import Queue


def negative_cycle(adj, cost):
    dist = [999999]*len(adj)
    prev = [None]*len(adj)
    dist[0] = 0

    # Bellman Ford
    for i in range(len(adj)):
        q = Queue()
        visited = []
        q.put(0)
        '''
        while not q.empty():
            node = q.get()
            visited.append(node)
            '''
        for node in range(len(adj)):
            for ind,neighbor in enumerate(adj[node]):
                #if neighbor not in visited:
                 #   q.put(neighbor)
                if dist[neighbor] > cost[node][ind] + dist[node]:
                    if i == len(adj)-1:
                        return 1
                    dist[neighbor] = cost[node][ind] + dist[node]
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    '''
    data = [10, 9,
1, 2, 1,
5, 6, 1,
6, 7, 1,
8, 9, 1,
9, 10, 1,
3, 4, 1,
7, 8, 1,
4, 5, 1,
2, 3, 1]'''

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
