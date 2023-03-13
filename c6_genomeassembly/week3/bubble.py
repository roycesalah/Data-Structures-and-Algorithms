# python3
import sys
import itertools

def main():
    data = sys.stdin.read().split()
    # k: k-mer size || t: bubble length threshold
    k,t,reads = data[0],data[1],data[2:]
    bubblecount = BubbleFind(int(k),int(t),reads)

class BubbleFind():
    def __init__(self,k,t,reads):
        self.k = k
        self.t = t
        self.kmers = self.reads2kmers(reads,k)
        self.debruijn = self.build_graph(self.kmers)
        self.bubble_search()
        #print(bubblecount)

    def reads2kmers(self,reads,k):
        kmers = []
        for read in reads:
            for i in range(len(read)-k+1):
                kmers.append(read[i:i+k])
        return kmers

    def build_graph(self,kmers):
        graph = dict()
        for kmer in kmers:
            kmer1,kmer2 = kmer[:-1],kmer[1:]
            if kmer1 != kmer2:
                if kmer1 not in graph:
                    graph[kmer1] = [set(),0]
                if kmer2 not in graph:
                    graph[kmer2] = [set(),0]
                if kmer2 not in graph[kmer1][0]:
                    graph[kmer1][0].add(kmer2)
                    graph[kmer2][1] += 1
        return graph

    def bubble_search(self):
        # Implement limited dfs function
        def dfs(self, path, start, current, depth):
            if path == None:
                path = [start]
            if current != start and self.debruijn[current][1] > 1:
                if (start, current) not in paths:
                    paths[(start,current)] = []
                paths[(start,current)].append(path[:])

            # If depth threshold is reached then return
            if depth == self.t:
                return

            # Recur dfs
            for neighbor in self.debruijn[current][0]:
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(self,path,start,neighbor,depth+1)
                    path.remove(neighbor)

        # Initialize path dict
        paths = dict()

        # DFS search each node with multiple outgoing edges
        for node,info in self.debruijn.items():
            outgoing = len(info[0])
            if outgoing > 1:
                dfs(self,None,node,node,0)

        bubblecount = 0

        for _, comb_vals in paths.items():
            for pair in list(itertools.combinations(comb_vals,2)):
                if len(set(pair[0]).intersection(set(pair[1]))) == 2:
                    bubblecount += 1

        print(bubblecount)


if __name__ == "__main__":
    main()