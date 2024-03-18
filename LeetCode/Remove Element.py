class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = []
        k = len(nums)

        for i in range(len(nums)):
            if nums[i] == val:
                k -= 1
                j.append(i)
            elif j:
                nums[j.pop(0)] = nums[i]
                j.append(i)

        return k
