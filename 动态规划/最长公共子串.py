#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here
        temp1 = 0
        res = ""
        for i in range(len(str1)):
            for j in range(len(str2)):
                length1 = 0
                temp=''          
                x=i
                y=j
                while x<len(str1) and y<len(str2) and str1[x]==str2[y]:
                    temp+=str1[x]
                    x+=1
                    y+=1                   
                    length1+=1
                if temp1<length1:
                    temp1 = length1
                    res = temp
        return res
                    
                    
        
        
        
        
        

                
            
            