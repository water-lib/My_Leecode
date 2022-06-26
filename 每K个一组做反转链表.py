# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        # write code here
        if head==None:
            return None
        cur2 = head
        l=0
        j=0
        zoombie = ListNode(0)
        zoombie.next = head
        pre = zoombie
        while cur2:
            l=l+1
            cur2 = cur2.next
        print(l)
        count = l//k
        print(count)
        while j<count:
            cur = pre.next
            for i in range(1,k):
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
            j=j+1
            pre = cur  
        return zoombie.next        