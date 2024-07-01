class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       array = {}
       for i, value in enumerate(nums): #1
           remaining = target - nums[i] #2
           
           if remaining in array: 
               return [i, array[remaining]]  
           else:
               array[value] = i 
    