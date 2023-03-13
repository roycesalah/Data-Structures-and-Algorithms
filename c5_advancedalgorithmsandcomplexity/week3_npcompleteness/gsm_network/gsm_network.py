# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula(n,m,edges):
    # Number of clauses
    C = n * 4 + m * 3
    # Number of variables
    V = n * 3
    print(C,V)

    # Exactly one color for each node
    for i in range(0,n):
        print("{} {} {} 0".format(3*i+1,3*i+2,3*i+3))
        print("{} {} 0".format(-(3*i+1),-(3*i+2)))
        print("{} {} 0".format(-(3*i+2),-(3*i+3)))
        print("{} {} 0".format(-(3*i+1),-(3*i+3)))

    # Exactly one of color in each edge
    for i in range(len(edges)):
        print("{} {} 0".format(-((edges[i][0]-1)*3+1),-((edges[i][1]-1)*3+1)))
        print("{} {} 0".format(-((edges[i][0]-1)*3+2),-((edges[i][1]-1)*3+2)))
        print("{} {} 0".format(-((edges[i][0]-1)*3+3),-((edges[i][1]-1)*3+3)))
        

printEquisatisfiableSatFormula(n,m,edges)
