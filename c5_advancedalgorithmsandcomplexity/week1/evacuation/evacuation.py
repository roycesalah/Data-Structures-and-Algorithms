# python3

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
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
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    '''
    
    vertex_count, edge_count = 5,7
    graph = FlowGraph(vertex_count)
    edges = [
        [1,2,2],
        [2,5,5],
        [1,3,6],
        [3,4,2],
        [4,5,1],
        [3,2,3],
        [2,4,1]
    ]
    for u,v,capacity in edges:
        graph.add_edge(u - 1, v - 1, capacity)
    '''
    return graph


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
    parent = [-1] *  graph.size()
    maxflow = 0
    while bfs(graph,from_,to,parent):
        pathflow = float("Inf")
        s = to
        while s != from_:
            edge = graph.edges[parent[s]]
            pathflow = min(pathflow,edge.capacity-edge.flow)
            s = edge.u
        maxflow += pathflow
        v = to
        while v != from_:
            edge = parent[v]
            graph.add_flow(edge,pathflow)
            v = graph.edges[edge].u

    return maxflow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
