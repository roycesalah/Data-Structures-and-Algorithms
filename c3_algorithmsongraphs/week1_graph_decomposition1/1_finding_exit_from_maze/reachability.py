#Uses python3

import sys

class Queue():
    def __init__(self):
        self.queue = []

    def empty(self):
        return self.queue == []

    def check_stack(self,node):
        return node in self.queue
    
    def add(self,node):
        self.queue.append(node)

    def remove(self):
        if self.empty():
            raise IndexError
        node = self.queue.pop(0)
        return node

def reach(adj, x, y):
    # Initialize stack and explored nodes set
    explored = set()
    queue = Queue()
    # Case when target node is starting node
    if x == y:
        return 1
    # Add starting node to queue
    queue.add(x)

    while True:
        if queue.empty():
            return 0
        node = queue.remove()
        explored.add(node)
        for neighbor in adj[node]:
            if neighbor not in explored:
                if neighbor == y:
                    return 1
                queue.add(neighbor)
        

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    '''
    x,y=0,3
    adj = [[1,3],[0,2],[3],[1,2]]
    '''
    print(reach(adj, x, y))
