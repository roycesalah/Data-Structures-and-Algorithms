# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.resultin = []
    self.inOrderRecur()
    return self.resultin

  def inOrderRecur(self,vertex=0):
    if vertex == -1:
      return
    self.inOrderRecur(self.left[vertex])
    self.resultin.append(self.key[vertex])
    self.inOrderRecur(self.right[vertex])

  def preOrder(self):
    self.resultpre = []
    self.preOrderRecur()
    return self.resultpre

  def preOrderRecur(self,vertex=0):
    if vertex == -1:
      return
    self.resultpre.append(self.key[vertex])
    self.preOrderRecur(self.left[vertex])
    self.preOrderRecur(self.right[vertex])

  def postOrder(self):
    self.resultpost = []
    self.postOrderRecur()         
    return self.resultpost

  def postOrderRecur(self,vertex=0):
    if vertex == -1:
      return
    self.postOrderRecur(self.left[vertex])
    self.postOrderRecur(self.right[vertex])
    self.resultpost.append(self.key[vertex])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
