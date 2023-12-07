#!/usr/bin/python3
'''A module for lockboxes.
'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened
    '''
    n = len(boxes)
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(set([0]))
    while len(locked_boxes) > 0:
        boxIndx = locked_boxes.pop()
        if boxIndx is None or boxIndx >= n or boxIndx < 0:
            continue
        if boxIndx not in unlocked_boxes:
            unseen_boxes = locked_boxes.union(boxes[boxIndx])
            unlocked_boxes.add(boxIndx)
            locked_boxes.update(unseen_boxes)
    return n == len(unlocked_boxes)
