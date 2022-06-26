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
# @return int整型二维数组
#
from collections import deque
class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        # write code here
        A=[]
        dq = deque([root])        
        if root==None:
            return A
        while dq:
            B=[]
            for _ in range(len(dq)):
                cur = dq.popleft()
                B.append(cur.val)
                if cur.left!=None:
                    dq.append(cur.left)
                if cur.right!=None:
                    dq.append(cur.right)
            A.append(B)
        return A
            
        