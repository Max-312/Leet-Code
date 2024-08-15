class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        storage = []
        for i in nums:
            if i-1 not in nums:
                left = i
                gap = 1
                while left + gap in nums:  
                    gap += 1
                if gap > 1:
                    storage.append(f"{i}->{left + gap - 1}")
                else:
                    storage.append(str(i))
        return storage