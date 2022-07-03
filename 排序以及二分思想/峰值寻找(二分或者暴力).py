#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def findPeakElement(self , nums: List[int]) -> int:
        # write code here
        #二分
        l=0
        r = len(nums)-1
        while l<r:
            m = int((l+r)/2)
            if nums[m]<nums[m+1]: #中点下个值比中点大，那么中点下一个值很可能是峰值点
                l=m+1
            else:
                r=m
        return r
                
          #暴力解法
#         if len(nums)==1:
#             return 0
#         elif len(nums)==2:
#             if nums[0]>nums[1]:
#                 return 0
#             else:
#                 return 1
#         if nums.index(max(nums))==0:
#             return 0
#         if nums.index(max(nums))==len(nums)-1:
#             return len(nums)-1
#         for i in range(1,len(nums)-2):
#             if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
#                 return i