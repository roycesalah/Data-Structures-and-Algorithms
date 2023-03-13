# python3
from itertools import combinations


n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula(n,m,edges):

    clauses = []

    # Each room belongs in the path exactly once
    for i in range(n):
        temp_clause = []
        # List of all possibilities of rooms at position in path
        for j in range(1,n+1):
            temp_clause.append(i*n + j)
        clauses.append(temp_clause)
        combs = list(combinations(temp_clause,2))
        # Negation clauses of combinations
        for combi in combs:
            clauses.append(list(map(lambda x: -x,combi)))

    # Each position is occupied by only one vertex
    for i in range(1,n+1):
        clause = [j * n + i for j in range(n)]
        clauses.append(clause)
        combs = list(combinations(temp_clause,2))
        # Negation clauses of combinations
        for combi in combs:
            clauses.append(list(map(lambda x: -x,combi)))

    vertices = list(range(1,n+1))
    # All possible edges
    APE = set(combinations(vertices,2))
    edges = set(map(tuple,edges))
    edges_rev = set()
    for edge in edges:
        edges_rev.add(tuple((edge[1],edge[0])))
    edges = edges.union(edges_rev)
    NPE = APE.difference(edges)
    for edge in NPE:
        for j in range(1,n):
            clauses.append([-((edge[0]-1)*n+j),-((edge[1]-1)*n+j+1)])
            clauses.append([-((edge[0]-1)*n+j+1),-((edge[1]-1)*n+j)])

    # Print C,V clauses
    C = len(clauses)
    V = n * n
    print(C,V)
    for clause in clauses:
        for i in clause:
            print(i,end=" ")
        print(0)


printEquisatisfiableSatFormula(n,m,edges)
