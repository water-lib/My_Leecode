#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param rotateArray int整型一维数组 
# @return int整型
#
class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        # write code here
        l=0
        r=len(rotateArray)-1
        #最小数一般会在右边，需要比较右边和中点
        while l!=r:
            m = int((l+r)/2)
            print(m)
            if rotateArray[m]>rotateArray[r]:#大了，中点加1赋予左节点
                l=m+1
            elif rotateArray[m]<rotateArray[r]:#小了，找到了，右节点直接给中点
                r=m
            else:
                r-=1
        return rotateArray[l]