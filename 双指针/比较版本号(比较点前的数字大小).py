#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 比较版本号
# @param version1 string字符串 
# @param version2 string字符串 
# @return int整型
#
class Solution:
    def compare(self , version1: str, version2: str) -> int:
        # write code here
        len_1 =len(version1)
        len_2 = len(version2)
        i,j = 0,0       
        while i<len_1 or j<len_1:
            num1 = 0 #某个version长度不够，则数字和为0
            while i<len_1 and version1[i]!='.':# 比较点前面的数字和大小
                num1 = num1*10+int(version1[i]) #求点之前的出数字和
                i=i+1
            i=i+1
            num2 = 0
            while j<len_2 and version2[j]!='.':
                num2 = num2*10+int(version2[j])
                j=j+1
            j=j+1
            if num1>num2:
                return 1
            elif num1<num2:
                return -1
        return 0