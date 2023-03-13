#Uses python3

import sys
    
def acyclic(adj):
    global sink
    sink = set()

    while True:
        # Check if all nodes are sinks, therefore no cycles
        if len(sink) == len(adj):
            return 0
        # Choose a new cycle checking point
        for node in range(len(adj)):
            if node not in sink:
                cycle_point = node
                break
        if detcycle(cycle_point,[]):
            return 1

def detcycle(node,disc):
    disc.append(node)
    global sink
    for neighbor in adj[node]:
        if neighbor in disc or (neighbor not in sink and detcycle(neighbor,disc)):
            return True
    sink.add(node)
    disc.remove(node)
    return False
    

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    '''
    n,m = 5,7
    edges = [(1,2),(2,3),(1,3),(3,4),(1,4),(2,5),(3,5)]
    '''
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
