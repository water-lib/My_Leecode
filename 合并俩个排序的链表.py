# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        head = ListNode(0)
        cur = head
        cur1 = pHead1
        cur2 = pHead2
        while cur1 and cur2 :
            if cur1.val<cur2.val:
                cur.next=cur1
                cur1=cur1.next
            else:
                cur.next=cur2
                cur2=cur2.next  
            cur = cur.next
        if cur1==None:
            cur.next = cur2
        if cur2==None:
            cur.next=cur1
        return head.next
            