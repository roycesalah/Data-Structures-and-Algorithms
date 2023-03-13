#!/usr/bin/python3

import sys, threading
import math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Check for empty tree
  vertices = []
  if tree == []:
    return True

  try:
    inOrderRecur()
    return True
  except:
    return False


def inOrderRecur(vertex=0,bst_range=[-math.inf,math.inf]):
  global tree
  if vertex == -1:
    return

  # Check left child and create ZeroDivisionError to break loop if False
  if not bst_range[0] <= tree[vertex][0] < bst_range[1]:
    1/0


  # Recursively check left and right children
  inOrderRecur(tree[vertex][1],[bst_range[0],tree[vertex][0]])
  inOrderRecur(tree[vertex][2],[tree[vertex][0],bst_range[1]])


def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
