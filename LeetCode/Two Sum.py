class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            m = target - n

            if n in hashMap:
                return [i, hashMap[n]]
            else:
                hashMap[m] = i
