#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 待判断的字符串
# @return bool布尔型
#
class Solution:
    def judge(self , str: str) -> bool:
        # write code here
        len_s = len(str)
        if len_s==1:
            return True
        l=0
        r=len_s-1
        while r>l:
            if str[l]!=str[r]:
                return False
            l=l+1
            r=r-1
        return True