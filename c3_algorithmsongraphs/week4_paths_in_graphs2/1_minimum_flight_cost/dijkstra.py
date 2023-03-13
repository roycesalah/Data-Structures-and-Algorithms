#Uses python3

import sys
from queue import PriorityQueue
import math


def distance(adj, cost, s, t):
    queue = PriorityQueue()
    dist = [math.inf] * len(adj)
    prev = [None] * len(adj)
    dist[s] = 0
    # Add s to queue with distance as the key in the pair
    queue.put((dist[s],s))
    while not queue.empty():
        node = queue.get()[1]
        for ind,neighbor in enumerate(adj[node]):
            if dist[neighbor] > dist[node] + cost[node][ind]:
                dist[neighbor] = dist[node] + cost[node][ind]
                prev[neighbor] = node
                queue.put((dist[neighbor],neighbor))
    if prev[t] != None:
        return dist[t]
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    '''
    data = [4, 4,
1, 2, 1,
4, 1, 2,
2, 3, 2,
1, 3, 5,
1, 3]'''
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
