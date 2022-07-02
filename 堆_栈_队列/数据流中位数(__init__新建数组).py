# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.A=[]
    def Insert(self, num):
        # write code here
        if len(self.A)==0:
            self.A.append(num)
        #插入排序 或直接sorted()
        else:
            i=0
            while i<len(self.A):
                if num<self.A[i]:
                    break
                i=i+1
            self.A.insert(i, num)
            print(self.A)
    def GetMedian(self):
        cnt = len(self.A)//2
        if len(self.A)==1:
            return self.A[0]
        if len(self.A)%2==0:
            return (self.A[cnt]+self.A[cnt-1])/2
        if len(self.A)%2!=0:
            return self.A[cnt]