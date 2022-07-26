#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#
class Solution:
    def threeSum(self , num: List[int]) -> List[List[int]]:
        # write code here
#         num = set(num)
        num = sorted(num)
        i=0
        result = []
        for i in range(len(num)-2):
            temp=num[i]
            r=len(num)-1
            l=i+1
            if i!=0 and num[i]==num[i-1]: #避免temp前后重复，将重复值写入
                    continue
            while l<r:
                if -(temp) == num[l]+num[r]: #双指针比较temp与末尾和temp+1的值
                    res=[temp,num[l],num[r]]
                    result.append(res)                 
                    while l<r and num[l]==num[l+1]: #去重，左右指针遇重复就跳过                      
                        l+=1                     
                    while r>l and num[r]==num[r-1]: #去重，左右指针遇重复就跳过                      
                        r-=1          
                    l+=1
                    r-=1
                elif -(temp) < num[l]+num[r]: #数组已经经过排序，双指针值小，移动左指针
                    r-=1
                else: #数组已经经过排序，双指针值大，移动右指针
                    l+=1
            print(l,r)
        return result