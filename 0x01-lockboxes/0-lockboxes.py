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
    if not boxes or type(boxes) is not list:
        return False

    n_boxes = len(boxes)
    unlocked = [False] * n_boxes
    unlocked[0] = True

    for i in range(n_boxes):
        if not Unlocked[i]:
            continue
        keys = boxes[i]
        for key in keys:
            if key >= n_boxes:
                continue
            if not unlocked[key]:
                unlocked[key] = True
    return all(unlocked)
