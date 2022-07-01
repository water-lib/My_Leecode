#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return bool布尔型
#
class Solution:
    def isValid(self , s: str) -> bool:
        # write code here
        if len(s)==1:
            return False
        A=[]
        for i in s:
            if i not in A: #栈中添加字符相对应的元素
                if i=="(":A.append(")")
                if i=="[":A.append("]")
                if i=="{":A.append("}")
                if i==")":A.append("(")
                if i=="]":A.append("[")
                if i=="}":A.append("{")
            else: #如果是最后没有正常闭合，那么最后pop出去一定会剩余
                A.pop()
        if A:
            return False
        else:
            return True
            