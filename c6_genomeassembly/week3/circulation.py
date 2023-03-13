# python3
class Edge:
    def __init__(self,u,v,lower,capacity):
        self.u = u
        self.v = v
        self.low = lower
        self.capacity = capacity-lower
        self.flow = 0
    

class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n+2)]
        self.minflow = [0]*(n+2)

    def add_edge(self, from_, to, lower, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, lower, capacity)
        backward_edge = Edge(to, from_, 0, 0)
        self.minflow[from_] += lower
        self.minflow[to] -= lower
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity += flow

def bfs2(graph, from_, to):
    pathflow = float('inf')
    queue = []
    queue.append(from_)

    n = len(graph.graph)
    dist = [float('inf')] * n
    path = []
    parent = [(None, None)] * n
    dist[from_] = 0

    solvable = False
    while len(queue) > 0:
        cur_node = queue.pop(0)
        for id in graph.graph[cur_node]:
            cur_edge = graph.edges[id]

            if float('inf') == dist[cur_edge.v] and cur_edge.capacity > 0:
                dist[cur_edge.v] = dist[cur_node] + 1
                parent[cur_edge.v] = (cur_node, id)
                queue.append(cur_edge.v)

                if cur_edge.v == to:
                    while True:
                        path.insert(0, id)
                        currX = graph.edges[id].capacity
                        pathflow = min(currX, pathflow)

                        if cur_node == from_:
                            break

                        cur_node, id = parent[cur_node]
                    solvable = True
                    return solvable, path, pathflow
    return solvable, path, pathflow

def max_flow2(graph, from_, to):
    flow = 0
    while True:
        solvable, path, pathflow = bfs2(graph, from_, to)
        if not solvable:
            return flow
        for id in path:
            graph.add_flow(id, pathflow)
        flow += pathflow


# Original unused approaches
def bfs(graph,from_,to,parent):
    visited = [False] * graph.size()
    # Initialize BFS queue
    queue = []

    # Append 
    queue.append(from_)
    visited[from_] = True

    while queue:
        node = queue.pop(0)
        for edge in graph.graph[node]:
            edge_ = graph.edges[edge]
            if visited[edge_.v] == False and edge_.flow < edge_.capacity:
                visited[edge_.v] = True
                queue.append(edge_.v)
                parent[edge_.v] = edge
                if edge_.v == to:
                    return True
    return False

def max_flow(graph, from_, to):
    parent = [-1] * graph.size()
    maxflow = 0
    while bfs(graph,from_,to,parent):
        pathflow = float("Inf")
        s = to
        while s != from_:
            edge = graph.edges[parent[s]]
            pathflow = min(pathflow,edge.capacity)
            s = edge.u
        maxflow += pathflow
        v = to
        while v != from_:
            edge = parent[v]
            graph.add_flow(edge,pathflow)
            v = graph.edges[edge].u

    return maxflow,graph
##


def main():
    vertex_count,edge_count = map(int,input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u,v,l,c = map(int,input().split())
        graph.add_edge(u - 1, v - 1, l, c)
    sink = 0
    for node in range(vertex_count):
        if graph.minflow[node] > 0:
            graph.add_edge(node,vertex_count,0,graph.minflow[node])
            sink += graph.minflow[node]
        elif graph.minflow[node] < 0:
            graph.add_edge(vertex_count+1,node,0,-graph.minflow[node])

    flow = max_flow2(graph, vertex_count + 1, vertex_count)
    if flow == sink:
        print("YES")
        for i in range(edge_count):
            print(graph.edges[i*2].flow+graph.edges[i*2].low)
    else:
        print("NO")




if __name__ == "__main__":
    main()