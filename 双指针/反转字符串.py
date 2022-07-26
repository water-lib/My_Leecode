#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 反转字符串
# @param str string字符串 
# @return string字符串
#
class Solution:
    def solve(self , str: str) -> str:
        # write code here
        if len(str)==0:
            return ""
        l=0
        r=len(str)-1
        res=''
        while r>=0:
            res=res + str[r]
            r=r-1
            print(res)
        return res