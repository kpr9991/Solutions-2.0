class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Time complexity n^2 space 1
        # for val in nums:
        #     if nums.count(val) > 1 :
        #         return True
        # return False
        
        # Time complexity n space n
        # dict={}
        # for val in nums:
        #     if dict.get(val):
        #         return True
        #     dict[val]=1
        
#         return False
        # Another time complexity n space complexity n
        return len(set(nums))<len(nums)
            
    
        
