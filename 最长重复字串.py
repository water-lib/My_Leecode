#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param a string字符串 待计算字符串
# @return int整型
#
class Solution:
    def solve(self , a: str) -> int:
        # write code here
        # write code here    
        max_len=0
        l=len(a)
        k=l//2
        while k>0:
                for i in range(l-2*k+1):
                    if(a[i:i+k] in a[i + k:i + 2 * k]):
                        return k*2
                k=k-1
        return 0
        