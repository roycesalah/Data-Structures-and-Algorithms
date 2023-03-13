# python3
import sys
import threading

# Discussion recommendation, stack overflow
sys.setrecursionlimit(10**6)
threading.stack_size(2**26)

def TwoSAT(graph,reverse,n):
    # Kosaraju's Algorithm
    # Find all SCCs
    scc,sccnum = SCC_search(graph,reverse,n)

    # Check for pos/neg literals in the same SCC
    for i in range(1, n + 1):
        if sccnum[i] == sccnum[i + n]:
            return False

    ans = [[] for _ in range(2*n+1)]
    avail = [False] * (2*n+1)
    for scci in scc:
        for v in scci:
            if not avail[v]:
                avail[v] = True
                ans[v] = 1
                if v > n:
                    ans[v - n] = 0
                    avail[v - n] = True
                else:
                    ans[v + n] = 0
                    avail[v + n] = True
    return ans

def SCC_search(graph,reverse,n):
    post = DFS(n,reverse)
    visited = [False] * (2 * n + 1)
    sccs = []
    sccnum = [0] * (2 * n + 1)
    j = 1
    for i in post:
        if not visited[i]:
            scc = []
            addSCC(i, j, graph, visited, scc, sccnum)
            sccs.append(scc)
            j += 1
    return sccs, sccnum

def addSCC(vertex, j, graph, visited, scc, sccnum):
    visited[vertex] = True
    scc.append(vertex)
    sccnum[vertex] = j
    for i in graph[vertex]:
        if visited[i] == False:
            addSCC(i, j, graph, visited, scc, sccnum)


def DFS(n, graph):
    # Initiaite global visit order number
    global visit
    visit = 1

    visited = [False] * (2*n + 1)
    postnum = [0] * (2*n+1)
    for v in range(1, 2*n+1):
        if not visited[v]:
            DFSrecur(v, graph, visited, postnum)
    postnum = list(enumerate(postnum[1:], start=1))
    postnum.sort(key=lambda x: x[1], reverse=True)
    postvis = []
    for v, order in postnum:
        postvis.append(v)
    return postvis

def DFSrecur(vertex,graph,visited,postnum):
    global visit
    visited[vertex] = True
    for i in graph[vertex]:
        if visited[i] == False:
            DFSrecur(i,graph,visited,postnum)
    postnum[vertex] = visit
    visit += 1




def main():
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]

    graph = [[] for _ in range(2*n + 1)]
    reverse = [[] for _ in range(2*n + 1)]
    # Create graphs
    for x,y in clauses:
        if x < 0 and y < 0:
            graph[-x].append(-y + n)
            graph[-y].append(-x + n)
            reverse[-y + n].append(-x)
            reverse[-x + n].append(-y)
        elif x > 0 and y > 0:
            graph[x + n].append(y)
            graph[y + n].append(x)
            reverse[y].append(x + n)
            reverse[x].append(y + n)
        elif x < 0 and y > 0:
            graph[-x].append(y)
            graph[y + n].append(-x + n)
            reverse[y].append(-x)
            reverse[-x + n].append(y + n)
        elif x > 0 and y < 0:
            graph[x + n].append(-y + n)
            graph[-y].append(x)
            reverse[-y + n].append(x + n)
            reverse[x].append(-y)

    result = TwoSAT(graph,reverse,n)

    if not result:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        for i in range(1,n+1):
            if result[i] > 0:
                print(i, end=' ')
            else:
                print(-i, end=' ')
    print("")





threading.Thread(target=main).start()