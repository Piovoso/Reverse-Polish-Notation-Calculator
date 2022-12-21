class Stack:
    def Append(list, *args): # Last In First Out
        for i in args: list.append(i)

    def Pop(list, count: int = 1): # Removes first value in Stack
        for i in range(count): list.pop(0)

    def PopPos(list, position: int = 0): # pops a specific index item in Stack
        list.pop(position)

    def PopRet(list): # Pops and removes the first item from the Stack
        item = list.pop(0)
        return item

    def Push(list, *args): # Pushes in a value into the Specific index in Stack
        for i in args: list.insert(0,i)

class Queue:
    def Enqueue(list, *args): # First in First out
        for i in args: list.append(i)

    def ForceQueue(list, position: int = 0 ,*args): # Forces an item into a Specific index in Queue
        for i in args: list.insert(position,i)

    def Dequeue(list, count: int = 1): # Removes last value in Queue
        for i in range(count): list.pop()

    def Rip(list): # Pops and removes the last item from the Stack
        item = list.pop(len(list)-1)
        return item
    
    def RipPos(list, position: int = 0): # Pops and removes the item at a specific index from the Stack
        item = list.pop(position)
        return item

class All: # Dunno, didn't use it, supposed to be similar to .All(char.isDigit) in C#
    def isDigit(*args):
        try:
            for i in args: int(i)
            return True
        except: return False