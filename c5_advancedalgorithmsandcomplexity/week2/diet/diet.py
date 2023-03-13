# python3
from sys import stdin
from itertools import combinations
from copy import deepcopy

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

def SelectPivotElement(step, used_rows, used_columns, a):
    pivot_element = Position(step, step)
    for i in range(step,len(used_columns)):
        if a[i][step] != 0:
            pivot_element.row = i
            return pivot_element
    return None
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
        if not pivot_element:
          return None
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

########################################################################################

def check_constraints(soln,eqn,m):
  # Iterate and check each condition
  for i in range(len(eqn.a)):
    eqn_sum = 0
    for j in range(m):
      eqn_sum += soln[j] * eqn.a[i][j]
    if eqn_sum - eqn.b[i] > 10**-3:
      return False
  return True


def solve_diet_problem(equation,subsets,pleasure,m):
  solns = []
  unbounded_solns = []
  for subset in subsets:
    # Create subset equations using subset indices
    a = []
    b = []
    unbounded = False
    for i in subset:
      a.append(deepcopy(equation.a[i]))
      b.append(deepcopy(equation.b[i]))
      if i == len(equation.a)-1:
        unbounded = True
    sub_eqn = Equation(a,b)
    soln = SolveEquation(sub_eqn)
    if soln != None:
      if check_constraints(soln,equation,m):
        if not unbounded:
          solns.append(soln)
        else:
          unbounded_solns.append(soln)


  # Return if no solution
  if not solns:
    return [-1,None]

  # Find best solution of bounded solutions
  best = -float("inf")
  best_soln = []
  for i in range(len(solns)):
    soln_pleasure = 0
    for j in range(m):
      soln_pleasure += solns[i][j] * pleasure[j]
    if soln_pleasure > best:
      best = soln_pleasure
      best_soln = solns[i]

  # Check if any unbounded solutions beat the best bounded
  for i in range(len(unbounded_solns)):
    soln_pleasure = 0
    for j in range(m):
      soln_pleasure += unbounded_solns[i][j] * pleasure[j]
    if soln_pleasure > best:
      return [1,None]

  return [0, best_soln]


def ReadEquation():
  # n restrictions and m foods/drinks
  n, m = list(map(int, stdin.readline().split()))
  # Create inequalities of form A*x <= b
  A = []
  for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
  b = list(map(int, stdin.readline().split()))

  pleasure = list(map(int, stdin.readline().split()))

  # Add in inequalities making all variables >= 0
  for i in range(m):
    grze = [0] * m
    grze[i] = -1
    A.append(grze)
    b.append(0)
  
  # Append a variable upperbound
  A.append([1]*m)
  b.append(10**9)

  subsets = list(combinations(range(len(A)),m))


  return Equation(A, b), subsets, pleasure, m


equation, subsets, pleasure, m = ReadEquation()
anst, ansx = solve_diet_problem(equation,subsets,pleasure,m)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
