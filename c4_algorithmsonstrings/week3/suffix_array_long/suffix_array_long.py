# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = sortcharacters(text)
  cls = computecharclass(text,order)
  L = 1
  while L < len(text):
    order = sortdouble(text,L,order,cls)
    cls = updateclasses(order,cls,L)
    L *= 2
  return order

def str2ind(str):
  return ["$","A","C","G","T"].index(str)

def sortcharacters(text):
  order = [0] * len(text)
  count = [0] * 5 ####

  for i in range(len(text)):
    count[str2ind(text[i])] += 1
  for j in range(1,len(count)):
    count[j] += count[j-1]
  for i in reversed(range(len(text))):
    c = text[i]
    cind = str2ind(c)
    count[cind] -= 1
    order[count[cind]] = i
  return order

def computecharclass(text,order):
  cls = [0] * len(text)
  cls[order[0]] = 0
  for i in range(1,len(text)):
    if text[order[i]] != text[order[i-1]]:
      cls[order[i]] = cls[order[i-1]] + 1
    else:
      cls[order[i]] = cls[order[i-1]]
  return cls

def sortdouble(text,L,order,cls):
  count = [0] * len(text)
  neworder = [None] * len(text)
  for i in range(len(text)):
    count[cls[i]] += 1
  for j in range(1,len(text)):
    count[j] += count[j-1]
  for i in reversed(range(len(text))):
    start = (order[i] - L + len(text)) % len(text)
    cl = cls[start]
    count[cl] -= 1
    neworder[count[cl]] = start
  return neworder

def updateclasses(neworder,cls,L):
  n = len(neworder)
  newcls = [None] * n
  newcls[neworder[0]] = 0
  for i in range(1,n):
    cur = neworder[i]
    prev = neworder[i-1]
    mid = (cur + L) % n
    midprev = (prev + L) % n
    if cls[cur] != cls[prev] or cls[mid] != cls[midprev]:
      newcls[cur] = newcls[prev] + 1
    else:
      newcls[cur] = newcls[prev]
  return newcls

      

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  #text = "AACGATAGCGGTAGA$"
  print(" ".join(map(str, build_suffix_array(text))))
