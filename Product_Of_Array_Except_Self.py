class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        prefix[0] = nums[0]
        postfix[len(nums)-1]=nums[-1]
        for i in range(1,len(nums)):
            prefix[i] = nums[i]*prefix[i-1]
        for j in range(len(nums)-2,-1,-1):
            postfix[j] = nums[j]*postfix[j+1]
        print(prefix, postfix)


        
