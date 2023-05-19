# Possible Combinations
# You are given N integers (12<N<20) in sorted order and your task is to print all the possible combinations of the numbers that can be used to choose 12 numbers out of the given N numbers in sorted order.
# Input Format:
# First line contains N - (Integer)
# Second line contains N spaced integers which are player Id of players. Note that, all the N integers are given in sorted order.
# Output Format:
# Print the space separated combinations in N lines
# Constraints
# 12<= N <= 20
# 1 <= Ai <=1000
# Sample Input :
# 13
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# Sample Output :
# 1 2 3 4 5 6 7 8 9 10 11 12
# 1 2 3 4 5 6 7 8 9 10 11 13 
# 1 2 3 4 5 6 7 8 9 10 12 13 
# 1 2 3 4 5 6 7 8 9 11 12 13 
# 1 2 3 4 5 6 7 8 10 11 12 13 
# 1 2 3 4 5 6 7 9 10 11 12 13 
# 1 2 3 4 5 6 8 9 10 11 12 13 
# 1 2 3 4 5 7 8 9 10 11 12 13 
# 1 2 3 4 6 7 8 9 10 11 12 13 
# 1 2 3 5 6 7 8 9 10 11 12 13 
# 1 2 4 5 6 7 8 9 10 11 12 13 
# 1 3 4 5 6 7 8 9 10 11 12 13 
# 2 3 4 5 6 7 8 9 10 11 12 13\


## Read input as specified in the question.
## Print output as specified in the question.
import itertools

N = int(input())
numbers = list(map(int, input().split()))

# Generate all combinations of choosing 12 numbers
combinations = list(itertools.combinations(numbers, 12))

# Print the combinations in sorted order
for comb in combinations:
    print(*comb)