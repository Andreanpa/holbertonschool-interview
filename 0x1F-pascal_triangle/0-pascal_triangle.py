#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's triangle of n
"""

def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle
    parameters:
        n [int]:
            the number of rows of Pascal's triangle to recreate
    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """
    if n <= 0: 
        return []
    
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for y in range(1. i):
            current = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(current)
        
        row.append(1)
        triangle.append(row)
    
    return triangle
