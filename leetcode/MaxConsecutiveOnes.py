class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prevSum = 0
        sum = 0
        for num in nums:
            if num == 1:
                sum += 1
            else:
                prevSum = max(prevSum, sum)
                sum = 0
        return max(prevSum, sum)