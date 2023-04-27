#!/usr/bin/python3
"""
You have and n number in front of you.
Each box is numbered sequentially
from 0 to n - 1 and eaxh box may
Contain keys to other boxes
"""
def join(T, R):
  res =[]
  for e in R:
    res += T[e]
  return res

def canUnlockAll(boxes):
  index = 0
  total = list(set(boxes[0]) | {0})
  added = True
  while added:
    added = False
    for j in join(boxes,total[indexe:]):
      if j not in total:
        total.append(j)
        index +=1
        added= True
  print(total)

  return len(total)==len(boxes)
