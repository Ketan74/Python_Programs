""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

"""Aim:-
    --> Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. 
    
    --> The Student class has data members such as those representing rollNumber, Name, etc. 
    
    --> Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored 
        in six subjects. 
        
    --> Derive Result from the Exam class, and it has its own fields such as total_marks.
    
    --> Write an interactive program to model this relationship."""

# ----------------------------------------------------------------------------------------------------------------------
# ***** SOLUTION ***** #
# ----------------------------------------------------------------------------------------------------------------------
class Student:
    def __init__(self, rollNumber, name, sem):
        self.rollNumber = rollNumber
        self.name = name
        self.sem = sem

    def display(self):
        print("\tRoll Number:-", self.rollNumber)
        print("\tName:-", self.name)
        print("\tSemester:-", self.sem)

class Exam(Student):
    def __init__(self, rollNumber, name, sem, marks):
        super().__init__(rollNumber, name, sem)
        self.mark = []
        for m in marks:
            self.mark.append(m)

    def display(self):
        super().display()
        n = 0
        for m in self.mark:
            print("\tMark for subject", n+1, "\b:-", m)
            n += 1


class Result(Exam):
    def __init__(self, rollNumber, name, sem, marks):
        super().__init__(rollNumber, name, sem, marks)
        self.total_marks = 0
        self.avg = 0
        for mark in marks:
            self.total_marks += mark
        self.avg = self.total_marks/6

    def display(self):
        super().display()
        print("\tTotal Marks:- ", self.total_marks)
        print("\tAvrage Marks:- ", self.avg)


numberOfStudent = int(input("Enter number of students:- "))
i = 0
obj = []
while i < numberOfStudent:
    print("Fill the following details for student", i+1)
    Name = input("\tEnter name of student:- ")
    roll_number = input("\tEnter roll number of student:- ")
    Sem = input("\tEnter semester of student:- ")
    Marks = []
    for j in range(6):
        print("\tEnter mark for subject", j+1, "\b:- ", end='')
        Mark = int(input())
        Marks.append(Mark)
    obj.append(Result(roll_number, Name, Sem, Marks))
    print()
    i += 1

i = 0
while i < numberOfStudent:
    print("Result of student", i+1)
    obj[i].display()
    print()
    i += 1