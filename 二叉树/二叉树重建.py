# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pre int整型一维数组 
# @param vin int整型一维数组 
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        if  len(pre)== 0 or len(vin) == 0:
            return None
        root_val = pre[0]
        A = TreeNode(root_val)
        inx = vin.index(root_val)
        A.left = self.reConstructBinaryTree(pre[1:inx+1], vin[0:inx])
        A.right = self.reConstructBinaryTree(pre[inx+1:], vin[inx+1:])
        return A