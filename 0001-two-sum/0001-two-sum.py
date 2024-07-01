class Solution(object):
    def twoSum(self, nums, target):
        array = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in array:
                return [array[t], i]
            array[num] = i
        return []