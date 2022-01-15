""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""
"""
    Aim:- Write a Python script to concatenate following dictionaries to create a new one:
          Sample Dictionary:- 
                dic1 = {1:10, 2:20}
                dic2 = {3:30, 4:40}
                dic3 = {5:50, 6:60}
          
          Expected Result:- {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
"""

dic1 = {1: 10, 2: 20}       # Initialized Dictionary 1
dic2 = {3: 30, 4: 40}       # Initialized Dictionary 2
dic3 = {5: 50, 6: 60}       # Initialized Dictionary 3

Merged_dic = dic1       # Initialized Merged Dictionary by Dictionary 1
Merged_dic.update(dic2)     # Merging Dictionary 2 into Merged Dictionary
Merged_dic.update(dic3)     # Merging Dictionary 3 into Merged Dictionary
print(Merged_dic)       # Printing Merged Dictionary