""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

"""Aim:-
    --> Lapindrome is defined as a string which when split in the middle, gives two halves having 
        the same characters and same frequency of each character. 
    --> If there are odd number of characters in the string, we ignore the middle character and 
        check for lapindrome.
    --> For example, gaga is a lapindrome, since the two halves ga and ga have the same characters
        with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes.
    --> Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their 
        frequencies do not match. 
    --> Your task is simple. Given a string, you need to tell if it is a lapindrome. 
    --> Sample Input: 
                6
                gaga 
                abcde 
                rotor 
                xyzxy 
                abbaab 
                ababc 
    --> Sample Output: 
                YES 
                NO 
                YES 
                YES 
                NO 
                NO"""

# ----------------------------------------------------------------------------------------------------------------------
# ***** SOLUTION ***** #
# ----------------------------------------------------------------------------------------------------------------------
number_of_words = int(input())        # Taking number of words
index = 0               # Index variable

while index < number_of_words:      # Loop for taking strings
    count = 0           # Flag variable
    in_string = input()         # storing ith word into the string variable

    if len(in_string) % 2 == 0:     # If length of string is even then slicing it into 2 parts
        _1_Part = list(in_string[0: int(len(in_string) / 2):])      # creating list of 1st part
        _2_Part = list(in_string[int(len(in_string) / 2): len(in_string):])     # creating list of 2nd part

    else:           # If length of string is odd then slicing in into to parts by ignoring middle character
        _1_Part = list(in_string[0: int(len(in_string) / 2):])      # creating list of 1st part
        _2_Part = list(in_string[int(len(in_string) / 2) + 1: len(in_string):])     # creating list of 2nd part

    for character in _1_Part:
        if _1_Part.count(character) == _2_Part.count(character):
            count += 1      # Increasing count by 1 when occurance of character in both part are same.

    if count == len(_1_Part):       # if value of count is same as length of 1st part then printing YES
        print('YES')

    else:                           # else printing NO
        print('NO')

    index += 1                  # Increasing index variable
# ----------------------------------------------------------------------------------------------------------------------