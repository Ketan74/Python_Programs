""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python script to merge two Python dictionaries.

Dictionary1 = {     # Initialized First Dictionary
    'First Name': 'Ketankumar',
    'Last Name': 'Tiwari',
    'Age': 19,
    'Country': 'India'
}
print('First Dictionary:- ')
for key in Dictionary1:
    print('\t', key, '\b:-', Dictionary1.get(key))

Dictionary2 = {     # Initialized Second Dictionary
    'Skills': ['C', 'C++', 'JAVA', 'Python'],
    'Is Married': False,
    'Address': {
        'Society': 'Matrupujan Society',
        'PIN Code': '388345'
    }
}
print('\nSecond Dictionary:- ')
for key in Dictionary2:
    print('\t', key, '\b:-', Dictionary2.get(key))

Merged_Dictionary = Dictionary1     # Initialized Third Dictionary Equal as First Dictionary
Merged_Dictionary.update(Dictionary2)   # Merging Second Dictionary in Merged Dictionary
print('\nMerged Dictionary:- ')
for key in Merged_Dictionary:
    print('\t', key, '\b:-', Merged_Dictionary.get(key))  # Printing Merged Dictionary