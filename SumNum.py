class Solution(object):
    def twoSum(self,nums,target):
        buff={}
        if len(nums)<=1:
            return False
        for i in range(len(nums)):
            if nums[i] in buff:
               return [buff[nums[i],i]]
            else:
            	buff[target-num[i]]=i
