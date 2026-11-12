class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(n)
        mapping = {}
        for i in range(len(nums)):
            cur = nums[i]
            x = target - cur
            if x in mapping:
                return [mapping[x], i]
            mapping[cur] = i
        return []