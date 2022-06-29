class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Solution1  O(n) space and O(N) Time Using dictionary of lists
        dict={}
        for i in range(0,len(nums)):
            if dict.get(nums[i]):
                dict[nums[i]].append(i)
            else:
                dict[nums[i]]=[i]
        for i in range(0,len(nums)):
            if nums[i]==target-nums[i]:
                if dict.get(nums[i]):
                    if(len(dict[nums[i]])>=2):
                        return [dict[nums[i]][0],dict[nums[i]][1]]
            else:
                if dict.get(target-nums[i]):
                    return [i,dict[target-nums[i]][0]]
         
        return []
                      
        # Solution 2 O(n^2)
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
#         return []
        
        
