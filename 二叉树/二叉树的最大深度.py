# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @return int整型
#
from collections import deque
class Solution:
    def maxDepth(self , root: TreeNode) -> int:
        # write code here
        if root == None:
            return 0
        dq = deque([root])
        cnt=0
        while dq:
            cnt+=1
            for _ in range(len(dq)):
                cur = dq.popleft()
                if cur.left :
                    dq.append(cur.left)
                if cur.right :
                    dq.append(cur.right)
        return cnt
        