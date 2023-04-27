#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes or ( type(boxes) != list):
        return 0
    keyList=[]
    hasMoreKeys = False
    countBoxes = len(boxes)
    boxesUnlock = setBoxesUnlock(countBoxes)
   
    for i in range(countBoxes):
        if( type(boxes[i]) == list ):
            if i == 0:
                keyList.append(0)
                setKeys(boxes[i], keyList)
           
            #print("i: {}, boxesUnlock[i]: {}, keyList: {}".format(i, boxesUnlock,keyList))
            if boxesUnlock[i] == 0 and keyList.count(i) > 0:
                #print("i: {}, boxesUnlock: {}, keyList: {}".format(i,boxesUnlock,keyList))
                unlockBox(keyList,boxesUnlock,boxes)
                #print("i: {}, boxesUnlock: {}, keyList: {}".format(i,boxesUnlock,keyList))

            if boxesUnlock.count(0) == 0:
                return True
    
    return False

def unlockBox(keys,boxesUnlock,boxes):
    keys_copy = keys
    for key in keys_copy:
        if key <= len(boxesUnlock):
            boxesUnlock[key] = 1
            setKeys(boxes[key],keys)
        keys.remove(key)

def setKeys(box, keyList):
    for key in box:
        if keyList.count(key) == 0:
            keyList.append(key) 

def setBoxesUnlock(count):
    boxes = []
    for i in range(count):
        boxes.append(0)
    return boxes       

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
