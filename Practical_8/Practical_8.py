""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

"""Aim:-
    --> Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and 
        traversal method."""

# ----------------------------------------------------------------------------------------------------------------------
# ***** SOLUTION ***** #
# ----------------------------------------------------------------------------------------------------------------------
class Stack:
    top = -1            # Index number of top of stack
    stack = []          # List Containing Elements of stack

    def pop(self):      # Method to pop out element from the stack
        if self.top < 0:        # If stack is empty...
            print("Underflow")
        else:
            self.stack.pop()
            self.top -= 1
            print("Pop Successed")

    def push(self, x):      # Method to push element into the stack
        self.stack.append(x)
        self.top += 1
        print("Push Successed")

    def traverse(self):     # Method to print elements of the stack
        i = self.top
        while i > -1:
            print(self.stack[i])
            i -= 1


print('Select option from below:-')
S1 = Stack()
while True:
    print('1. Push\n2. Traverse\n3. Pop\n4. Exit')
    choice = int(input('Enter your choice:- '))

    if choice == 1:     # Push Operation
        x = int(input('Enter number to push:- '))
        S1.push(x)
        print()

    elif choice == 2:   # Printing Data
        S1.traverse()
        print()

    elif choice == 3:   # Pop Operation
        S1.pop()
        print()

    elif choice == 4:   # Exiting From the menu
        break

    else:
        print('Select valid option')
        choice = int(input('Enter your choice:- '))