#
# 
# @param A int整型一维数组 
# @param B int整型一维数组 
# @return void
#
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        if len(B)==0:
            return A
        if len(A)==0:
            return B
        l=m+n
        k = l-1
        i=  m-1
        j= n-1
        while i>=0 and j>=0:
            if A[i]>B[j]:
                A[k]=A[i]
                i=i-1
                k=k-1
            else:
                A[k]=B[j]
                j=j-1
                k=k-1
        if i<0:
            while j>=0:
                A[k] = B[j]
                j=j-1
                k=k-1
                
        
        