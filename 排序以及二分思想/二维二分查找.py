#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param target int整型 
# @param array int整型二维数组 
# @return bool布尔型
#
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        if len(array[0])==0:
            return False
        # write code here
        for i in array:
            l=0
            r=len(i)-1
            while l<=r:
                m=int((l+r)/2)
                if target == i[m]: 
                    return True
                elif target > i[m]:
                    l=m+1
                else:
                    r=m-1
        return False