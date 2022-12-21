from RPN import Stack, Queue


class calculator:
    def __init__(self, equation):
        QueueList = []
        StackList = []
        for char in equation:
            calculator.ShuntingYard(char, StackList, QueueList)
        
        print(f'Stack {StackList}\nQueue {QueueList}')
        print(calculator.ReversePolishNotation(StackList, QueueList))


    def ShuntingYard(char, stack, queue):
        try:
            value = int(char)
            if len(queue) > len(stack): value = str(Queue.Rip(queue)) + str(value)
            Queue.Enqueue(queue, value)
        except:
            if len(queue) <= len(stack): char = str(Stack.PopRet(stack)) + char
            Stack.Append(stack, char)

    def ReversePolishNotation(stack, queue):
        while True:
            if len(queue) == 1: return queue[0]

            if '**' in stack:
                index = stack.index('**')
                math = int(Queue.RipPos(queue, index)) ** int(Queue.RipPos(queue, index))
                Queue.ForceQueue(queue, index, math)
                Stack.PopPos(stack, index)

            elif '/' in stack or '*' in stack:
                if '*' in stack and stack.index('*') < stack.index('/'):
                    index = stack.index('*')
                    math = int(Queue.RipPos(queue, index)) * int(Queue.RipPos(queue, index))
                    Queue.ForceQueue(queue, index, math)
                    Stack.PopPos(stack, index)
                else:
                    index = stack.index('/')
                    math = int(Queue.RipPos(queue, index)) / int(Queue.RipPos(queue, index))
                    Queue.ForceQueue(queue, index, math)
                    Stack.PopPos(stack, index)

            elif '+' in stack or '-' in stack:
                if '+' in stack and stack.index('+') < stack.index('-'):
                    index = stack.index('+')
                    math = int(Queue.RipPos(queue, index)) + int(Queue.RipPos(queue, index))
                    Queue.ForceQueue(queue, index, math)
                    Stack.PopPos(stack, index)

                else:
                    index = stack.index('-')
                    math = int(Queue.RipPos(queue, index)) - int(Queue.RipPos(queue, index))
                    Queue.ForceQueue(queue, index, math)
                    Stack.PopPos(stack, index)

UserInput = input('Math equation: ')
new = calculator(UserInput)