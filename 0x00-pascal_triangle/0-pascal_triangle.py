#!/usr/bin/python3
""" Pascal Triangle  """


def pascal_triangle(n):
    """
    calculates pascals triangle for the a list
    """
    if type(n) is not int:
        raise TypeError("n must be an interger")
    triangle = []
    if n <= 0:
        return triangle
    previous = [1]
    for row_index in range(n):
        rowlist = []
        if row_index == 0:
            rowlist = [1]
        else:
            for i in range(row_index + 1):
                if 1 == 0:
                    rowlist.append(0 + previous[i])
                elif i == (row_index):
                    rowlist.append(previous[i - 1] + 0)
                else:
                    rowlist.append(previous[i - 1] + previous[1])
        previous = rowlist
        triangle.append(rowlist)
    return triangle
