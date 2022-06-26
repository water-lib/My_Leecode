# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        # write code here
        if head==None:
            return None
        cur = head
        while cur and cur.next:
            if (cur.val == cur.next.val):
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
                

                
        