# Quadruplet Sum
# Given an array nums of n integers and integer x, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == x
# Store all such possible quadruplets in an 2D array, and return it. The order of the quadruplets does not matter.
# Input Format:
# First line of input contains an integer n, representing the size of the array.
# Second line of input contains n space separated integers.
# Third line of input contains an integer x.
# Constraints:
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Output Format:
# Return all possible quadruplets
# Sample Input 1:
# 6
# 1 0 -1 0 -2 2 
# 0
# Sample Output1:
# -2 -1 1 2   
# -2 0 0 2
# -1 0 0 1


def fourSum(nums, target):
    nums.sort()  # Sort the array in ascending order
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates for the first number

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicates for the second number

            left = j + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates for the third and fourth numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result

# Taking input
n = int(input()))
nums = list(map(int, input().split()))
x = int(input())

# Calling the function
quadruplets = fourSum(nums, x)

for i in range(len(quadruplets)):
    for j in range(4):
        print(quadruplets[i][j],end=" ")
    print(" ")