# Break Numbers
# Given an integer n, break it into smaller numbers such that their summation is equal to n. Print all such combinations in different lines.
# Note : [1, 2, 1] and [1,1, 2] are same, so print the particular sequence with increasing order. Order of different combinations doesn't matter.
# Input format :
# Integer n
# Output format :
# Print all possible combinations in different lines
# Constraints :
# 1 <= n <= 100
# Input :
# 4
# Output :
# 1 1 1 1
# 1 1 2
# 1 3
# 2 2
# 4

from os import *
from sys import *
from collections import *
from math import *

def breakNumber(n):
    # Write your code here.
    arr = list(range(1, n + 1))
    res = []

    def backtrack(idx, target, tmp):
        if target == 0:
            res.append(tmp[:])
            return
        
        if idx == n or target < 0:
            return
        
        for i in range(idx, len(arr)):
            tmp.append(arr[i])
            backtrack(i, target - arr[i], tmp)
            tmp.pop()
 
    backtrack(0, n, [])
    return res

n = int(input())
ans = breakNumber(n)
for i in ans:
    nAns = i
    nA = ""
    for j in nAns:
        nA += str(j)+ " "
    print(nA)
    # print(str(nAns))
    # print(type(nAns))
    