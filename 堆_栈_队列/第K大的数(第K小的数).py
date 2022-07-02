#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param a int整型一维数组 
# @param n int整型 
# @param K int整型 
# @return int整型
#
class Solution:
    def findKth(self , a: List[int], n: int, K: int) -> int:
        # write code here
        #栈的先进先出思想，保持只有K个元素，大于栈顶的元素重新（最大的数在栈底）
        #放栈底，栈顶始终是第K大（只有K个元素）。第K小 n-K+1
        #内置函数解决
        a.sort(reverse=True)
        return a[K-1]
        
        
#快排思想        
#         return self.quicksort(a, 0, n-1, K)
#     def quicksort(self,a,start,end,k):
#         if start>end:
#             return -1
#         t = a[start]
#         l = start
#         r = end
#         while r>l:
#             while r>l and a[r]<=t: #第K大的数,因此要相反，大的在左边，小的在右边
#                 r-=1
#             while r>l and a[l]>=t:#第K小的数，则直接套用快排，a[l]<=t,小的在左边
#                 l+=1
#             if l!=r:
#                 a[l],a[r]=a[r],a[l]
#         a[start],a[l]=a[l],a[start]
#         if l==k-1:
#             return a[l]
#         elif l<k-1:
#             return self.quicksort(a, l+1, end, k)
#         else:
#             return self.quicksort(a, start, l-1, k)
        
        
        
                    
            
        
        
        