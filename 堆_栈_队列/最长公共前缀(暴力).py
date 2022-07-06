#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param strs string字符串一维数组 
# @return string字符串
#
class Solution:
    def longestCommonPrefix(self , strs: List[str]) -> str:
        # write code here
        if not strs:
            return ""
        first_num = strs[0]
        len1 = len(first_num)
        B=[]
        cnt=0
        if len(strs)==1:
            return first_num
        for i in range(1,len(strs)):
            B.append(strs.pop())
        print(B)
        while len1 > 0:
            for i in range(len(B)):
                if first_num[0:len1] in B[i]:
                    cnt += 1
                    if cnt == len(B):
                        return first_num[:len1] #first_num[:0] 在任何情况下都为"" 空
                else:
                    len1 = len1 - 1
                    break
        return first_num[:len1] #不满足上面条件 return null