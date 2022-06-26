# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self , head: ListNode) -> bool:
        # write code here
        list_A=[]
        cur = head
        while cur:
            list_A.append(cur.val)
            cur = cur.next
        length = len(list_A)
        for i in range(0,length):
            if list_A[i]!=list_A[length-1-i]:
                return False
            else:
                pass
        return True
                