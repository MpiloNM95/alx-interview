#!/usr/bin/python3
"""
Solution for the locboxes problem
"""


def caUnlockAll(boxes):
    """
    Determine if all boxes can be opened by checking if there is a path from box 0 to all other boxes.

    Args:
    _ boxes: A list of lists of integers. Each inner list represents a box and contains the indices of the boxes it can open.

    Returns: 
    - True if all boxes can be opened. False otherwise
    """
    n = len(boxes)
    unlocked_boxes = set([0])
    keys = set(boxes[0]) 

    while keys and len(unlocked_boxes) < n:
        key = keys.pop()
        if key < n and key not in unlocked_boxes: 
            unlocked_boxes.add(key)
            keys.update(boxes[key]) 

    return len(unlocked_boxes) == n
