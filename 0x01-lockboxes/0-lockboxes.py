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
    unlocked_boxes = set([0]) # Keeps track of boxes that have been unlocked so far
    keys = set(boxes[0]) # Keys initially available to unlock other boxes

    
    # Keep on trying to unlock more boxes until the boxes are unlocked all of them or until the boxes cant be unlock anymore
    while keys and len(unlocked_boxes) < n:
        key = keys.pop()
        if key < n and key not in unlocked_boxes: # Check if the key opens a box we haven't unlocked yet 
            unlocked_boxes.add(key)
            keys.update(boxes[key]) # Add the key in the unlocked box to the collection of available keys

    return len(unlocked_boxes) == n
