""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python program to add an item in a tuple.

tuple1 = (range(5))     # Initialized Tuple 1 by using range function
item = input("Enter a item you want to add in tuple:- ")        # Taking item to add in tuple
list1 = list(tuple1)        # Converting tuple to list
list1.append(item)      # Adding item to list
tuple1 = tuple(list1)       # Converting list to tuple
print(tuple1)       # Printing Tuple