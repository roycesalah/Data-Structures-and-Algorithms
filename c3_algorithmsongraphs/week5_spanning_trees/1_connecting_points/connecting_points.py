#Uses python3
import sys
import math
import queue

def minimum_distance(x, y):
    # Create list of nodes
    nodes = set()
    for i in range(len(x)):
        nodes.add((x[i],y[i]))

    result = 0.

    # Initialize priority queue and used nodes set
    q = queue.PriorityQueue()
    q.put((0,(x[0],y[0])))
    used = set()

    # Iterate through all nodes with Prim's Algorithm
    while len(used) != len(nodes):
        distance,node = q.get()
        if node in used:
            continue
        result += distance
        used.add(node)
        for neighbor in nodes.difference(used):
            neighbor_dist = ((node[0]-neighbor[0])**2 + (node[1]-neighbor[1])**2)**0.5
            q.put((neighbor_dist,neighbor))
    
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [5,0,0,0,2,1,1,3,0,3,2]
    #data = [4,0,0,0,1,1,0,1,1]
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
