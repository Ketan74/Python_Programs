""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

""" Aim:- Mr. Anant is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
          One fine day, a finite number of tourists come to stay at the hotel.
          The tourists consist of:
            → A Captain.
            → An unknown group of families consisting K of  members per group where  K ≠ 1.
          The Captain was given a separate room, and the rest were given one room per group. 
          Mr. Anant has an unordered list of randomly arranged room entries. 
          The list consists of the room numbers for all of the tourists.
          The room numbers will appear K times per group except for the Captain's room. 
          Mr. Anant needs you to help him find the Captain's room number. 
          The total number of tourists or the total number of groups of families is not known to you. 
          You only know the value of K and the room number list.
          
          Input Format:- The first line consists of an integer, K , the size of each group.
                         The second line contains the unordered elements of the room number list.
          
          Constraints:- 1< K<1000
          
          Output Format:- Output the Captain's room number.
          
          Sample Input:- 5
                         1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
      
          Sample Output:- 8
      
          Explanation:- The list of room numbers contains 31 elements. 
                        Since K is 5, there must be 6 groups of families. 
                        In the given list, all of the numbers repeat 5 times except for room number 8.
                        Hence,  8 is the Captain's room number."""

# ----------------------------------------------------------------------------------------------------------------------
# ***** SOLUTION ***** #
# ----------------------------------------------------------------------------------------------------------------------
members_per_group = int(input())        # Taking value of K
lst = input().split()         # Taking input in a list
room_numbers = {}      # crated dictionary key = room number and value = occurrence of that number
check = 0       # Flag variable
i = 0
# ----------------------------------------------------------------------------------------------------------------------
for item in lst:
    if int(item) in room_numbers.keys():    # If key exist in dictionary then increasing value of that key by 1
        room_numbers[int(item)] = room_numbers.get(int(item)) + 1
    else:       # If key is not exist then inserting that key and value of that key initializing by 1
        room_numbers[int(item)] = 1


for key in room_numbers:
    if room_numbers.get(key) == 1:      # If any key is having value 1 is a room number of captain
        print(key)          # Printing Room Number of Captain
        break
# ----------------------------------------------------------------------------------------------------------------------