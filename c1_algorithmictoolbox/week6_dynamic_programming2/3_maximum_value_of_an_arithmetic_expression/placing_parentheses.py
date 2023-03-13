def evaluate(a, b, op):
    if op == '+':
        return (a + b)
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    n = (len(dataset)+1)//2
    global M,m
    M = dict() # Minimum
    m = dict() # Maximum
    for i in range(1,n+1):
        m.update({(i,i):int(dataset[2*i-2])})
        M.update({(i,i):int(dataset[2*i-2])})
    for s in range(1,n):
        for i in range(1,n-s+1):
            j = i+s
            # Min and Max
            m[(i,j)],M[(i,j)] = MinMax(i,j,dataset)
    return M[(1,n)]

def MinMax(i,j,dataset):
    mins = 99999
    maxs = -99999
    global M,m
    for k in range(i,j):
        opk = dataset[(k*2)-1]
        a = evaluate(M[(i,k)],M[(k+1,j)],opk)
        b = evaluate(M[(i,k)],m[(k+1,j)],opk)
        c = evaluate(m[(i,k)],M[(k+1,j)],opk)
        d = evaluate(m[(i,k)],m[(k+1,j)],opk)
        mins = min(mins,a,b,c,d)
        maxs = max(maxs,a,b,c,d)
    return (mins,maxs)


if __name__ == "__main__":
    print(maximum_value(input()))
