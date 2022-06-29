# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # write code here
        return self.stack1.pop()
    def top(self):
        # write code here
        return self.stack1[-1]
    def min(self):
        print({"1","1"})
        # write code here #min()可以求数组中最小值，同理max。或者numpy中list.min(0/1)
        return min(self.stack1)
    #数组去重--> list(set(listA)) 转化为集合，集合无重复
                   # for i in listA:
                        #if i not in listB:
                            # listB.append(i)
    #求出数组中重复--> 去重后的与未去重的对比：list_quchong in list_noqu: list_noqu.remove()