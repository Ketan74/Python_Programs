""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

"""Aim:-Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
        You are given n scores. Store them in a list and find the score of the runner-up.
        
        Input Format:- The first line contains n.
                       The second line contains an array A[]  of n integers each separated by a space.
                       
        Constraints:-
        
        Output Format:- Print the runner-up score.
        
        Sample Input:- 5
                       2 3 6 6 5

        Sample Output:- 5

        Explanation:- Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5.
                      Hence, we print 5 as the runner-up score."""

# ----------------------------------------------------------------------------------------------------------------------
# ***** SOLUTION ***** #
# ----------------------------------------------------------------------------------------------------------------------
n = int(input())        # Taking value of n
A = list(map(int, input().strip().split()))[:n]         # Taking array of scores
i = 0
maximum = 0
# ----------------------------------------------------------------------------------------------------------------------
while i < n:                    # Finding           |
    if i == 0:                  # Maximum           |
        maximum = A[i]          # Value             V
    elif maximum < A[i]:        # In                |
        maximum = A[i]          # Given             |
    i += 1                      # Score list        V
# ----------------------------------------------------------------------------------------------------------------------
j = 0
while maximum in A:             # Removing all occurrence       |
    A.remove(maximum)           # of that maximum value         |
    j += 1                      # from given score list         V
# ----------------------------------------------------------------------------------------------------------------------
i = 0
while i < n-j:                  # Again finding             |
    if i == 0:                  # Maximum                   |
        maximum = A[i]          # value in updated          V
    elif maximum < A[i]:        # score list                |
        maximum = A[i]          # which is nothing but      |
    i += 1                      # runner-up score           V
# ----------------------------------------------------------------------------------------------------------------------
print(maximum, end='')          # Printing runner-up score
# ----------------------------------------------------------------------------------------------------------------------