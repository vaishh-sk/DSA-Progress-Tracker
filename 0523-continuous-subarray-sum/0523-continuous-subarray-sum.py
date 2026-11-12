class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_map={0:-1}
        x=0
        for i,num in enumerate(nums) :
            x+=num
            remainder=x%k 
            if remainder in remainder_map :
                if i-remainder_map[remainder]>=2:
                    return True
            else :
                remainder_map[remainder]=i
        return False
nums=[23,2,6,4,7]
k=6
sol=Solution()
r=sol.checkSubarraySum(nums,k)
print(r)