from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <=1:
            return size
        pSlow=0
        for pFast in range(1,size):
            if nums[pFast] != nums[pSlow]:
                pSlow+=1
                nums[pSlow] = nums[pFast]
        return pSlow+1

if __name__ == '__main__':
    nums = [1,2,2,3,4,4,5]
    print(Solution().removeDuplicates(nums))

            

