# Power
# Ninja is given an easy task. He has to implement a function which calculates a^b. But there is a small difference, b is an extremely large positive number given in the form of an array.
# Note: Since answers can be huge, print answer mod 1337.
# It is given that b will not contain leading zeros.
# Input Format:
#  First line of input contains an integer a
#  Second line of input contains an integer n, representing the size of the array.
#  Third line of input contains an array (space separated).
# Constraints:
# 1 <= a <= 2^31 - 1
# 1 <= b.length <= 3 * 10^6
# 0 <= b[i] <= 9
# Time Limit: 1 second
# Output Format:
# Single line of output printing a^b
# Sample Input 1:
# 5
# 2
# 1 5
# Sample Output:
# 944
# Explanation:
# 5 to the power 15 is 30517578125. Its mod with 1337 is 944.


from functools import reduce


def superPow(a,b):
    # Compute a_mod = a mod 1337
    a_mod = a % 1337
    
    # Compute n, the number represented by the array b, using reduce()
    n = reduce(lambda x, y: (x * 10 + y) % 1140, b, 0)
    
    # Compute a_mod raised to the power of n using repeated squaring
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * a_mod) % 1337
        a_mod = (a_mod * a_mod) % 1337
        n //= 2
    
    # Return the result modulo 1337
    return result % 1337
a = int(input())
n = int(input())
b = list(map(int, input().split()))
ans = superPow(a,b)
print(ans)