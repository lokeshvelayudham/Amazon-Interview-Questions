# We are given a series of Binary Strings. The first term in this series is 0. Hence, T1 = '0'.
# To find the string at any given Ti, we look at Ti - 1 and replace all occurances of '0' with '01' and '1' with '10'.
# You are given two integers N and X, your job is to find TN and return its Xth index.
# Note: Ti are 1-indexed.
# Input Format:
# First line of input contains an integer T, representing the number of test cases.
# The next T lines contains two space separated integers, N and X.
# Constraints:
# Output Format:
#  Print the Xth index in Nth row
# Sample Input:
# 1
# 4 5 
# Sample Output:
# 1
# Explanation:
# T1: '0'
# T2: '01'
# T3: '0110'
# T4: '01101001'
# The 5th element in T4 is '1'.


def find_character(N, X):
    if N == 1:
        return "0" if X == 1 else "1"
    
    mid = 2**(N-1)
    if X <= mid:
        return find_character(N-1, X)
    else:
        return "1" if find_character(N-1, X-mid) == "0" else "0"

# Taking input
T = int(input())

for _ in range(T):
    N, X = map(int, input().split())

    # Calling the function
    result = find_character(N, X)
    print(result)
