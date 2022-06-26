#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 给定数组的最长严格上升子序列的长度。
# @param arr int整型一维数组 给定的数组
# @return int整型
#
class Solution:
    def LIS(self , arr: List[int]) -> int:
        # write code here   
        dp = [0 for i in range(len(arr))]
        res = 0
        len_arr = len(arr)
        for i in range(len_arr):
            dp[i]=1
            for j in range(0,i):
                if arr[i]>arr[j]:
                    dp[i]=max(dp[j]+1, dp[i])
                    res = max(dp[i],res)
        return res
                
        