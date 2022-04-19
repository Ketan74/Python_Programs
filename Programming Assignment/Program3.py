""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""


def maximumArea(a1, lenOfArr):
    Area = 0

    for i in range(lenOfArr):
        for j in range(i + 1, lenOfArr):
            Area = max(Area, min(a1[j], a1[i]) * (j - i))

    return Area


a = [int(n) for n in input("Enter an array: ").split()]

lenOfArr = len(a)
print(maximumArea(a, lenOfArr))