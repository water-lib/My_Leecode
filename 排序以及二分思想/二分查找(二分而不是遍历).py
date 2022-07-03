#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here
        if len(nums)==0:
            return -1
        l=0
        r=len(nums)-1
        while r>=l:
            if r>=l and nums[l]==target:
                return l
            if r>=l and nums[r]==target:
                return r
            l+=1
            r-=1
        return -1
        