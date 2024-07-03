class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        array ={}
        for i, value in enumerate(numbers):
            remaining = target - numbers[i]

            if remaining in array:
                return array[remaining] + 1, i + 1
            else:
                array[value] = i
