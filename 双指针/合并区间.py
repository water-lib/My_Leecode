# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param intervals Interval类一维数组 
# @return Interval类一维数组
#
class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:
        # write code here
        if len(intervals)==0:return []
        intervals.sort(key= lambda x:x.start)
        res=[intervals[0]]
        
        for i in intervals[1:]:
            if i.start>res[-1].end:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end,i.end)
        return res
            
            
        
        
                