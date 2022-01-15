""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python program to create an intersection, Union, difference of sets.

set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}       # Initialized Set 1
set2 = {0, 2, 4, 6, 8, 10, 12, 14}              # Initialized Set 2
set3 = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}     # Initialized Set 3
set4 = {1, 3, 5, 7, 9, 11}                      # Initialized Set 4
print('Intersection of', set1, 'And', set2, 'is:- ', set1.intersection(set2))       # Intersection of set 1 and set 2
print('Union of', set1, 'And', set3, 'is:- ', set1.union(set3))     # Union of set 1 and set 3
print('Difference of', set1, 'From', set4, 'is:- ', set1.difference(set4), end='')      # Difference of set 1 and set 4