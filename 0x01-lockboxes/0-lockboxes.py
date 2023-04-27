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
    opened_boxes = set()
    opened_boxes.add(0)
    keys = set(boxes[0])
    while keys and opened_boxes != set(range(n)):
        key = keys.pop()
        if key < n and key not in opened_boxes:
            opened_boxes.add(key)
            keys.update(boxes[key])
    return opened_boxes == set(range(n))
