""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python script to check whether a given key already exists in a dictionary.

Given_Key = input("Enter a key:- ")     # Taking key as an input
Dictionary = {      # Initialized one Dictionary
    'First Name': 'Ketankumar',
    'Last Name': 'Tiwari',
    'Age': 19,
    'Country': 'India',
    'Skills': ['C', 'C++', 'JAVA', 'Python'],
    'Is Married': False,
    'Address': {
        'Society': 'Matrupujan Society',
        'PIN Code': '388345'
    }
}
value = 0   # Flag
for key in Dictionary:
    if Given_Key == key:    # Checking key exists in a Dictionary or not
        print('Given Key Already Exists In A Dictionary.', end='')
        value = 1
        break
if value == 0:  # For printing message that key doesn't exist in a Dictionary
    print('Given Key Not Exists In A Dictionary.', end='')