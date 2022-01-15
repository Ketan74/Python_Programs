""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python program to remove an item from a set if it's present in the set.

set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}       # Initialized Set 1
value = 0       # Flag variable
Check = 'Y'     # Flag variable
while Check == 'Y':
    element = int(input("Enter a element you want to remove from the set:- "))  # Taking element for Removing from the set
    for item in set1:
        if item == element:     # Checking that item is present in a set or not
            set1.remove(element)        # Removing item from the Set 1
            print('Entered element removed successfully...')
            value = 1
            break
    if value == 0:      # If element not found in the set
        print('Entered element is not exist in the set')
    Check = input("If you want to remove more item then press \"Y\":- ")
    print()
print(set1)     # Printing Set 1 after removing elements