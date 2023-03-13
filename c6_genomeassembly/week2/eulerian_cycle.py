# python3

class Node():
    def __init__(self,nodenum):
        self.nodenum = nodenum
        self.neighbors = []

    def visit(self,neighbor):
        self.neighbors.remove(neighbor)

    def empty(self):
        return len(self.neighbors) == 0

def FindEulerianCycle(nodes,m):
    cycle = [nodes[0]]
    edgecount = 0
    while edgecount < m:
        if cycle[-1].empty():
            for i in range(len(cycle)):
                if not cycle[i].empty():
                    cycle = [cycle[i]] + cycle[i+1:] + cycle[1:i+1]
                    break
        else:
            edgecount += 1
            if edgecount == m:
                break
            next = cycle[-1].neighbors[0]
            cycle[-1].visit(next)
            cycle.append(next)
    return cycle

def main():
    n,m = list(map(int,input().strip().split()))
    nodes = [Node(i) for i in range(n)]
    balance = [0 for _ in range(n)]
    for d in range(m):
        n1,n2 = list(map(int,input().strip().split()))
        nodes[n1-1].neighbors.append(nodes[n2-1])
        balance[n2-1] += 1
        balance[n1-1] -= 1
    if any(balance):
        print(0)
    else:
        eu = FindEulerianCycle(nodes,m)
        print(1)
        for node in eu:
            print(node.nodenum+1,end=" ")
        print()


if __name__ == "__main__":
    main()