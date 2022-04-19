""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

str1 = input()

freq = {}
for item in str1:
    if item in freq.keys():
        freq[item] = freq.get(item) + 1
    else:
        freq[item] = 1

lst1 = []
for item in freq:
    lst1.append([freq.get(item), item])

lst1.sort(reverse=True)

for item in lst1:
    print(item[1], item[0])
