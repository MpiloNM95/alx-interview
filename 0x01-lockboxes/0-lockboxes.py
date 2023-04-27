#!/usr/bin/python3
"""
Solution for the locboxes problem
"""


def caUnlockAll(boxes):
    """
    To see if all locked boxes can be opened using 
    the code below.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for ids in range(len(boxes)):
            boxes_checked = k in boxes[ids] and k != ids
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
