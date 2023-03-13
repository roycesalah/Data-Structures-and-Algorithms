#Uses python3

import sys
import queue
import math


def distance(adj, s, t):
    # Initialize visited list, parent list, and queue
    q = queue.Queue()
    distance = [math.inf] * len(adj)
    q.put(s)
    distance[s] = 0

    while q.qsize() != 0:
        node = q.get()
        for neighbor in adj[node]:
            if neighbor == t:
                return distance[node] + 1
            if distance[neighbor] == math.inf:
                q.put(neighbor)
                distance[neighbor] = distance[node] + 1

    return -1

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    
    #n,m = 4,4 #
    #edges = [(1,2),(4,1),(2,3),(3,1)] #
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    #s,t = 1,3 #

    print(distance(adj, s, t))
