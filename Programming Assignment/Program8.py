""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""


class Parent:

    def show(self):
        print("Inside Parent")


class Child(Parent):
    def show(self):
        print("Inside Child")


obj = Child()

obj.show()
