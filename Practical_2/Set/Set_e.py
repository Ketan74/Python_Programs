""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
print('For List:- ')
lst = [1, 1, 2, 3, 4, 1, 4, 2, 4, 5]        # Initialized List
value = 0       # Flag Variable
count = {}      # Dictionary for item and it's count
for item in lst:        # For counting the occurrence of each element
    for item2 in lst:
        if item2 == item:
            value = value + 1
            count[item] = value
    value = 0
for key in count:       # Printing elements and their occurrence in List
    print('\tElement:-', key, '\tCount:-', count.get(key))

print('\nFor Tuple:- ')
tuple1 = ('Python', 'C', 'C++', 'C', 'Java', 'C', 'Python')     # Initialized Tuple
value = 0       # Flag Variable
count = {}      # Dictionary for item and it's count
for item in tuple1:     # For counting the occurrence of each element
    for item2 in tuple1:
        if item2 == item:
            value = value + 1
            count[item] = value
    value = 0
for key in count:       # Printing elements and their occurrence in Tuple
    print('\tElement:-', key, '\tCount:-', count.get(key))

print('\nFor Dictionary:- ')
Dictionary = {     # Initialized Dictionary
    'Player 1': 'Ketan',
    'Player 2': 'Dhruvin',
    'Player 3': 'Pratik',
    'Player 4': 'Pratham',
    'Player 5': 'Pratik',
    'Player 6': 'Pratham'
}
value = 0       # Flag Variable
count = {}      # Dictionary for item and it's count
for key in Dictionary:           # For counting the occurrence of each element
    for key2 in Dictionary:
        if Dictionary.get(key2) == Dictionary.get(key):
            value = value + 1
            count[Dictionary.get(key)] = value
    value = 0
for key in count:       # Printing elements and their occurrence in Dictionary
    print('\tElement:-', key, '\tCount:-', count.get(key))