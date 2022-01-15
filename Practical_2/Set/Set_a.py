""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python program to add member(s) in a set and clear a set.

set1 = {1, 2, 3}        # Initialized Set 1
Check = 'Y'     # Flag Variable
while Check == 'Y':
    element = input("Enter a element you want to add in set:- ")    # Taking element to add in the Set 1
    set1.add(element)       # Adding element to Set 1
    Check = input("If you want to add more item then press \"Y\":- ")
    print()
print(set1)     # Printing Set 1

Check = input("If you want to clear the set then press \"Y\":- ")
if Check == 'Y':
    set1.clear()        # Clearing Set 1
print(set1)     # Again Printing Set 1