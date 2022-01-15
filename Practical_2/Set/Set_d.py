""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python program to find maximum and the minimum value in a set.

set1 = {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}       # Initialized Set 1
MAX = 0     # Maximum element in Set
MIN = 0     # Minimum element in Set
for item in set1:       # For Finding max and min in Set
    if item > MAX:
        MAX = item
    elif item < MIN:
        MIN = item

print('Maximum value in a set is:- ', MAX)      # Printing max
print('Minimum value in a set is:- ', MIN)      # Printing min
