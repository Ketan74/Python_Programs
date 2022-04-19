""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

from itertools import combinations as comb

Numbers = [int(n) for n in input("Enter element: ").split()]

k = int(input("Enter the value of K : "))

count = 0

for i in range(1, len(Numbers) + 1):

    for c in comb(Numbers, i):
        if sum(c) == k:
            count += 1

print(count)