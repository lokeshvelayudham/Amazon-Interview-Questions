# Maximum Subarray Sum
# This problem was asked by Amazon.
# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
# Given the array [-5, -1, -8, -9], the maximum sum would be -1.
# Follow up: Do this in O(N) time.
# Input Format:
# The first line of input contains size of array, which is denoted by N and second line of input contains N space separated integers.
# Output Format:
# The first and only line of output should print the maximum subarray sum, as described in the description.


#Write your code here
def max_subarray_sum(arr):
    max_sum = arr[0]  # Initialize max_sum with the first element
    curr_sum = arr[0]  # Initialize curr_sum with the first element

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

n = int(input())
arr = list(map(int, input().split()))
print(max_subarray_sum(arr))