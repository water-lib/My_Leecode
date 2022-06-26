# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param m int整型 
# @param n int整型 
# @return ListNode类
#
class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        zoombie = ListNode(0)
        zoombie.next = head
        pre = zoombie
        for i in range(1,m):
            pre = pre.next
        cur = pre.next
        for i in range(m,n):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return zoombie.next

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            




        