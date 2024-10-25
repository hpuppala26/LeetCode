class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sums = 0
        start = 0
        temp = 0
        end = len(nums)-1
        max_sums = max(nums)
        for i in range(len(nums)):
            sums = sums + nums[i]
            if sums > max_sums:
                max_sums = sums
                start = temp
                end = i
            if sums < 0:
                sums = 0
                temp = i+1
        print(start,end)
        return max_sums
            

        
#This is the best Solution -- The print statements print the start and end index of the subarray so that we can print if the question is modified.
#We use here Kadene Algorithm.
