#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param height int整型一维数组 
# @return int整型
#
class Solution:
    def maxArea(self , height: List[int]) -> int:
        # write code here
        if len(height)<2:
            return 0
        l=0
        r=len(height)-1
        max_=0
        while r>l:
            area = min(height[l],height[r])*(r-l)
            max_ = max(area,max_)
            if height[l]>height[r]:
                r=r-1
            else:
                l=l+1
        return max_
        

                    