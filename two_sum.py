class Solution(object):
    def twoSum(self, nums, target):
         hashmap={}
         for i in range(len(nums)):
                compliment=target-nums[i]
                
                if compliment in hashmap:
                    return [hashmap[compliment], i]
                hashmap[nums[i]] = i
