# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param pHead1 ListNodeš▒╗ 
# @param pHead2 ListNodeš▒╗ 
# @return ListNodeš▒╗
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        set_A = set()
        cur = pHead1
        cur2 = pHead2
        while cur:
            set_A.add(cur)
            cur = cur.next
        while cur2:
            if cur2 in set_A:
                return cur2
            else:
                cur2 = cur2.next
        

            