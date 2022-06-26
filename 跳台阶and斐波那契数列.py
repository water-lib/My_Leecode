#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code
        dp=[0 for i in range(number+4)]
        for i in range(number+1):
            if i==0 or i==1:
                dp[i]=1
                print(dp[i])
            else:
                dp[i]=dp[i-1]+dp[i-2]
                print(dp[i])
        return dp[number]
