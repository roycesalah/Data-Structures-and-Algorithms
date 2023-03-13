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
    kmer = int(input().strip())
    nodes = [Node((bin(i)[2:].zfill(kmer))) for i in range(2**kmer)]
    for i in range(2**kmer):
        nodes[i].neighbors.append(nodes[i*2%(2**(kmer-1))])
        nodes[i].neighbors.append(nodes[i*2%(2**(kmer-1))+1])

    eu = FindEulerianCycle(nodes,2**kmer)
    for node in eu:
        print(int(node.nodenum)%2,end="")
    print()


if __name__ == "__main__":
    main()