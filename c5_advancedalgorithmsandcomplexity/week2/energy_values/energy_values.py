# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        # a are variables
        # b is answer
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(step, used_rows, used_columns, a):
    pivot_element = Position(step, step)
    for i in range(step,len(used_columns)):
        if a[i][step] != 0:
            pivot_element.row = i
            return pivot_element
    return pivot_element
    '''
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    return pivot_element'''

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    num = a[pivot_element.row][pivot_element.column]

    # Reduce the pivot row
    for i in range(len(a[0])):
        a[pivot_element.row][i] /= num
    b[pivot_element.row] /= num

    # Iterate through rows and "substitute" the value so the value is canceled
    for row in range(len(a)):
        if row != pivot_element.row and a[row][pivot_element.column] != 0:
            scale = a[row][pivot_element.column]
            for col in range(pivot_element.column,len(a[0])):
                a[row][col] -= a[pivot_element.row][col] * scale
            b[row] -= b[pivot_element.row] * scale

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size

    for step in range(size):
        pivot_element = SelectPivotElement(step, used_rows, used_columns, a)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
