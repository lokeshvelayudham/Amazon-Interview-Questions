# Given two integers a and b. You need to find and return the count of possible ways in which we can represent the number a as the sum of unique integers raise to the power b.
# For example: if a = 10 and b = 2, only way to represent 10 as sum of unique integers raised to power 2 is-
# 10 = 1^2 + 3^2 
# Hence, answer is 1.
# Note : x^y represents x raise to the power y
# Input Format:
# The first line of input contains two space separated integers, that denote the value of a and b.
# Output Format:
# The first and only line of output contains count of ways in which a can be represented as sum of unique integers raised to power b.
# Constraints :
# 1 <= a <= 10^4
# 1 < b <= 20
# Time Limit: 1 second
# Sample Input 1 :
# 10 2
# Sample Output 1 :
# 1
# Sample Input 2 :
# 100 2
# Sample Output 2 :
# 3
# Explanation:
# Following are the three ways: 
# 1. 100 = 10^2
# 2. 100 = 8^2 + 6^2
# 3. 100 = 7^2+5^2+4^2+3^2+1^2

from sys import stdin , setrecursionlimit
setrecursionlimit(10**8)

def power(num, n):
 
    if(n == 0):
        return 1
    elif(n % 2 == 0):
        return power(num, n // 2) * power(num, n // 2)
    else:
        return num * power(num, n // 2) * power(num, n // 2)
 
# Function to check power representations recursively
 
 
def checkRecursive(x, n, curr_num=1, curr_sum=0):
 
    # Initialize number of ways to express
    # x as n-th powers of different natural
    # numbers
    results = 0
 
    # Calling power of 'i' raised to 'n'
    p = power(curr_num, n)
    while(p + curr_sum < x):
 
        # Recursively check all greater values of i
        results += checkRecursive(x, n, curr_num + 1, p + curr_sum)
        curr_num = curr_num + 1
        p = power(curr_num, n)
 
    # If sum of powers is equal to x
    # then increase the value of result.
    if(p + curr_sum == x):
        results = results + 1
 
    # Return the final result
    return results





# Main
a,b = [int(x) for x in stdin.readline().strip().split()] 
print(checkRecursive(a,b))