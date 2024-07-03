class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       array = {}
       for i, value in enumerate(nums): 
           remaining = target - nums[i] 
           
           if remaining in array: 
               return [array[remaining], i]  
           else:
               array[value] = i 
    