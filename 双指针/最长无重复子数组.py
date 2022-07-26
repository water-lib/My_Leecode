#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr: List[int]) -> int:
        # write code here
        if len(arr)==1:
            return 1
        a=[arr[0]]
        max_=1
        len_a=0
        for i in arr[1:]:
            if i in a:
                a=a[a.index(i)+1:]#从重复后的下一位开始新的数组，不能直接清空
                a.append(i)
            else:
                a.append(i)
                len_a=len(a)
                max_=max(max_,len_a)
        return max_
        