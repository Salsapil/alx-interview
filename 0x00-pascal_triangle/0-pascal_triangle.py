#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle.
    
    n: The number of rows to generate.
    return: A list of lists, where each list represents a row in Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
