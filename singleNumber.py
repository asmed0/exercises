def singleNumber(nums: list[int]) -> int:
    temp = []
    for i in range(len(nums)):
        if nums[i] not in temp:
            temp.append(nums[i])
        elif nums[i] in temp:
            temp.remove(nums[i])

    return temp[0]


class Solution:
    pass


print(singleNumber(nums=[4, 1, 2, 1, 2]))
