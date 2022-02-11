""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

"""Aim:-
    --> You are given n words. Some words may repeat.
    --> For each word, output its number of occurrences.
    --> The output order should correspond with the input order of appearance of the word.
    --> See the sample input/output for clarification. 
    --> Sample Input:- 
            4 
            bcdef
            abcdefg
            bcde
            bcdef
    --> Sample Output:- 
            3 
            2 1 1 
    --> Explanation:- 
            --> There are 3 distinct words.
            --> Here, "bcdef" appears twice in the input at the first and last positions.
            --> The other words appear once each.
            --> The order of the first appearances are "bcdef", "abcdefg" and "bcde" which 
                corresponds to the output."""

# ----------------------------------------------------------------------------------------------------------------------
# ***** SOLUTION ***** #
# ----------------------------------------------------------------------------------------------------------------------
num_words = int(input())        # Taking number of words
index = 0               # Index variable
words = {}              # Created dictionary for taking word as a key and store their occurance as value

while index < num_words:        # Loop for taking words
    in_string = input()            # storing ith word into the string variable
    if in_string in words.keys():  # If dictionary words contains given word then increasing its value
        words[in_string] += 1
    else:                       # Else adding given word as a key with value 1
        words[in_string] = 1
    index += 1                  # Increasing index variable

print(len(words))           # length of words gives us distinct words inputed

for key in words:
    print(words.get(key), end=' ')      # Printing occurance of all words.
# ----------------------------------------------------------------------------------------------------------------------