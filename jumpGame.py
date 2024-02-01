# JumpGame - You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position. Return true if you can reach
# the last index, or false otherwise.

# Example:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Solution: Let n refill our jumps_left by the amount of steps we can jump, iterate over nums and whenever n+1 > n
# replace jumps_left with n+1 amount of jumps Enumerate this until jumps_left <= 0. If here jumps_left >= len(nums)
# we have reached our destination successfully

def canJump(nums: list[int]) -> bool:
    jumps_left = 0
    for n in nums:
        if jumps_left < 0:
            return False
        elif n > jumps_left:
            jumps_left = n
        jumps_left -= 1
    return True


class Solution:
    pass


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([0]))
print(canJump([0, 1]))
