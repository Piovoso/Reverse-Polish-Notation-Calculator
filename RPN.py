class Stack:
    def Append(list, *args): # Last In First Out
        for i in args: list.append(i)

    def Pop(list, count: int = 1): # Removes first value in list
        for i in range(count): list.pop(0)

    def PopPos(list, position: int = 0):
        list.pop(position)

    def PopRet(list):
        item = list.pop(0)
        return item

    def Push(list, *args):
        for i in args: list.insert(0,i)

class Queue:
    def Enqueue(list, *args): # First in First out
        for i in args: list.append(i)

    def ForceQueue(list, position: int = 0 ,*args):
        for i in args: list.insert(position,i)

    def Dequeue(list, count: int = 1): # Removes last value in list
        for i in range(count): list.pop()

    def Rip(list): # retruns the last value in list, and removes it
        item = list.pop(len(list)-1)
        return item
    
    def RipPos(list, position: int = 0):
        item = list.pop(position)
        return item

class All:
    def isDigit(*args):
        try:
            for i in args: int(i)
            return True
        except: return False