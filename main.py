from RPN import Stack, Queue

class calculator:
    def __init__(self, expression): # initialising Calculator
        QueueList = []
        StackList = []
        for char in expression: # Seperating Expression to Characters for processing
            calculator.ShuntingYard(char, StackList, QueueList) # Passing Required Items to ShuntingYard function

        print(calculator.ReversePolishNotation(StackList, QueueList)) # Prints the returned value from ReversePolishNotation Function on line 27.

    def ShuntingYard(char, stack, queue):
        try: # Just here to catch if the string is convertable to integer
            value = int(char)
            if len(queue) > len(stack): # Checks if item is a two or more digit number or not by comparing list lenghts
                value = str(Queue.Rip(queue)) + str(value)

            Queue.Enqueue(queue, value) # Adds the character value into the Queue

        except: # String Conversion exception, Mathematical operator
            if len(queue) <= len(stack): # Checks if it is the Power operator **
                char = str(Stack.PopReturn(stack)) + char 
            Stack.Append(stack, char)

    def ReversePolishNotation(stack, queue): # Actual Calculating
        while True:
            if len(queue) == 1: return queue[0] #Returns the Final value left in the stack

            if '**' in stack: # Power, following code is the exact same for other mathematical operators
                index = stack.index('**') # Indexes the Operator (single digit)
                math = int(Queue.RipPosition(queue, index)) ** int(Queue.RipPosition(queue, index)) # Does the calculation by Riping out the Corresponding values in the position of Operator
                Queue.ForceQueue(queue, index, math) # Forces the math value back into it's index value in the queue
                Stack.PopPosition(stack, index) # Removes the Operator from the stack.

            elif '/' in stack or '*' in stack: # Equal Mathematical operators
                if '*' in stack and stack.index('*') < stack.index('/'): # Checks which one comes first in the stack.
                    index = stack.index('*') # following in stated on lines 30 - 33
                    math = int(Queue.RipPosition(queue, index)) * int(Queue.RipPosition(queue, index))
                    Queue.ForceQueue(queue, index, math)
                    Stack.PopPosition(stack, index)
                else:
                    index = stack.index('/') # following in stated on lines 30 - 33
                    math = int(Queue.RipPosition(queue, index)) / int(Queue.RipPosition(queue, index))
                    Queue.ForceQueue(queue, index, math)
                    Stack.PopPosition(stack, index)

            elif '+' in stack or '-' in stack: # Equal Mathematical operators
                if '+' in stack and stack.index('+') < stack.index('-'): # Checks which one comes first in the stack.
                    index = stack.index('+') # following in stated on lines 30 - 33
                    math = int(Queue.RipPosition(queue, index)) + int(Queue.RipPosition(queue, index))
                    Queue.ForceQueue(queue, index, math)
                    Stack.PopPosition(stack, index)

                else: 
                    index = stack.index('-') # following in stated on lines 30 - 33
                    math = int(Queue.RipPosition(queue, index)) - int(Queue.RipPosition(queue, index))
                    Queue.ForceQueue(queue, index, math)
                    Stack.PopPosition(stack, index)

UserInput = input('Math equation: ')
new = calculator(UserInput)
