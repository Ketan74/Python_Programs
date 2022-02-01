""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

"""Aim:-You are given a string and your task is to swap cases. 
        In other words, convert all lowercase letters to uppercase letters and vice versa.
        Sample Input:- 
                HackerRank.com presents "Pythonist 2".

        Sample Output:-
                hACKERrANK.COM PRESENTS "pYTHONIST 2"."""

# ----------------------------------------------------------------------------------------------------------------------
# ***** SOLUTION ***** #
# ----------------------------------------------------------------------------------------------------------------------

def swap(string):                       # Function to swap the case of string
    str2 = ''
    for letter in string:
        if letter.islower():            # If letter is lower...
            str2 += letter.upper()      # Adding letter into str2 after converting it case to upper case
        elif letter.isupper():          # If letter is upper...
            str2 += letter.lower()      # Adding letter into str2 after converting it case to lower case
        else:
            str2 += letter              # If letter is not alphabet then adding it in str2 directly
    return str2                         # Returning str2


str1 = input('Enter String:- ')         # Taking string as a input
print(swap(str1))                       # Printing returning value by call of swap(str1)
# ----------------------------------------------------------------------------------------------------------------------