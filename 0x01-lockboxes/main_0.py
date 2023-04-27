#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes), "\t: True \t 1")
print('-----------------------------')

boxes = [[1, 4, 6], [2, 0], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes), "\t: True \t 2")
print('-----------------------------')

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes),  "\t: False  3")
print('-----------------------------')

boxes = [[1,3],[3,0,1],[2],[0]]
print(canUnlockAll(boxes),  "\t: False  4")
print('-----------------------------')

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6], [7]]
print(canUnlockAll(boxes), "\t: False  5")
print('-----------------------------')

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6], [7]]
print(canUnlockAll(boxes), "\t: False  6")
print('-----------------------------')

boxes = [[2], [3, 4], [1, 5]]
print(canUnlockAll(boxes), "\t: True \t 7")
print('-----------------------------')

boxes = [[2]]
print(canUnlockAll(boxes), "\t: True \t 8")
print('-----------------------------')

boxes = []
print(canUnlockAll(boxes), "\t: False  9")
print('-----------------------------')

boxes = [[1, 2, 3], [], [], [], []]
print(canUnlockAll(boxes), "\t: False  10")
print('-----------------------------')

boxes = None
print(canUnlockAll(boxes), "\t: False  11")
print('-----------------------------')

boxes = 'hello, is it me you looking for?'
print(canUnlockAll(boxes), "\t: False  12")
print('-----------------------------')

boxes = [[0, 4, 4], [5], [3], [1], [2], [5]]
print(canUnlockAll(boxes), "\t: True \t 13")
print('-----------------------------')

boxes = [[1, 4], [2], [0, 4, 1], [6], [3], [4, 1], [5, 6], [7]]
print(canUnlockAll(boxes), "\t: False  14")
print('-----------------------------')

boxes = [[1], [1], [1]]
print(canUnlockAll(boxes), "\t: False  15")
print('-----------------------------')

boxes = [[], [2], [4]]
print(canUnlockAll(boxes), "\t: False  16")
print('-----------------------------')

boxes = [[0, 1], [2, 3], {}, None]
print(canUnlockAll(boxes), "\t: False  17")
print('-----------------------------')

boxes = [[]]
print(canUnlockAll(boxes), "\t: True \t 18")
print('-----------------------------')

boxes = [[1, 2], ['hey', 'you'], ['sup']]
print(canUnlockAll(boxes), "\t: True \t 19")
print('-----------------------------')

boxes = [{}, [2, 3], {}, None]
print(canUnlockAll(boxes), "\t: False  20")
print('-----------------------------')

boxes = [[0, 1], [2, 3], [7, 4], [2]]
print(canUnlockAll(boxes), "\t: True \t 21")
print('-----------------------------')

boxes = [{}]
print(canUnlockAll(boxes), "\t: False  22")
print('-----------------------------')

boxes = [[2]]
print(canUnlockAll(boxes), "\t: True \t 23")
print('-----------------------------')

boxes = [[], [1, 2, 7], [0, 3]]
print(canUnlockAll(boxes), "\t: False  24")
print('-----------------------------')


#  X    X    X    X    X
#[[1], [2], [3], [4], []]
#  0    1    2    3   4

#     X       X       X          X       X     X      X
#[[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
#     0       1       2          3       4      5     6

#  X       X       X            X
#[[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
#   0      1       2       3    4     5       6
