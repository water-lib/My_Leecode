#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @param n int整型 
# @return string字符串
#
class Solution:
    def trans(self , s: str, n: int) -> str:
        # write code her
        A=[]
        res = ''
        A = s.swapcase().split(' ')[::-1]
        for i in A:
            res=res+i+" "
        return res[:-1]
        