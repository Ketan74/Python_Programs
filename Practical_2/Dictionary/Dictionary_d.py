""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
# Aim:- Write a Python script to add a key to a dictionary.

Dictionary = {
}
Check = 'Y'     # Flag Variable
print('Enter Your Dictionary items:- ')     # Taking items in Dictionary
while Check == 'Y':
    key = input("\tEnter a Key:- ")
    value = input("\tEnter a Value:- ")
    Dictionary[key] = value     # Adding items in Dictionary
    Check = input("\tIf you want to add more items then press \"Y\":- ")
    print()

Check = input("If you still want to add item to dictionary then press \"Y\":- ")
if Check == 'Y':
    key_add = input("Enter a key:- ")
    value_add = input("Enter a value:- ")
    Dictionary[key_add] = value_add     # Adding items in Dictionary
print(Dictionary, end='')