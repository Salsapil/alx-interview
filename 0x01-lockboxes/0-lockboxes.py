#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """all boxes are checked and the traversal stops
    as soon as all reachable boxes are visited"""
    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        box = queue.pop(0)
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key not in visited and key < n:
                    queue.append(key)

    return len(visited) == n
