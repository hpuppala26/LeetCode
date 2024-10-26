class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]:
                if target > nums[middle]:
                    left = middle + 1
                elif target < nums[middle] and target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if target < nums[middle]:
                    right = middle - 1
                elif target > nums[middle] and target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1

        
