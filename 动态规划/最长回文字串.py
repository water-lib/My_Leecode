#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param A string字符串 
# @return int整型
# #self 表示Solution self调Solution
class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        # write code here
        res=1
        for i in range(0,len(A)-1):
            res = max(res,Solution.fun1(A,i,i),Solution.fun1(A,i,i+1))
        return res    
    def fun1(A,begin,end):
            while begin>=0 and len(A)>end and A[begin]==A[end]:
                begin-=1
                end+=1
            return end-begin-1
