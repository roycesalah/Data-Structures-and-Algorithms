# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  S = pattern + "$" + text
  s = computeprefix(S)
  result = []
  for i in range(len(pattern),len(S)):
    if s[i] == len(pattern):
      result.append(i-2*len(pattern))
  return result

def computeprefix(S):
  s = [0]*len(S)
  border = 0
  for i in range(1,len(S)):
    while border > 0 and S[i] != S[border]:
      border = s[border-1]
    if S[i] == S[border]:
      border += 1
    else:
      border = 0
    s[i] = border
  return s


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  #pattern,text = "A","A"
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

