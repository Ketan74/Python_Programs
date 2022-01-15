""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python program to sum all the items in a dictionary.

Dictionary = {      # Initialized Dictionary
    '1': 10,
    '2': 20,
    '3': 30,
    '4': 40,
    '5': 50
}
Total = 0       # Variable to store sum of all items
for key in Dictionary:
    Total += Dictionary.get(key)        # Adding all items in variable Total

print('Sum of all items is:-', Total, '\b.')        # Printing Sum of all items