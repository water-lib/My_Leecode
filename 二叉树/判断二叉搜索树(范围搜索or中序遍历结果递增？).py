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
# @return bool布尔型
#
class Solution:
    def isValidBST(self , root: TreeNode) -> bool:
        return self.fun(root, [-float("inf"),float("inf")])
    def is_in_range(self,root,range_):
        return range_[0]<root.val<range_[1]
    def fun(self,root,range_):
        print(range_[0])
        if root==None:
            return True
        if not self.is_in_range(root,range_):
            return False
        left = self.fun(root.left,[range_[0],root.val])
        right = self.fun(root.right,[root.val,range_[1]])
        return left and right
    
            
    
#         A=[]
#         self.fun(A, root)
#         l = len(A)
#         if l==1:
#             return True
#         for i in range(l-1):
#             if A[i]>A[i+1]:
#                 return False
#         return A
#     def fun(self,A,root):
#         if root==None:
#             return 
#         self.fun(A, root.left)
#         A.append(root.val)
#         self.fun(A,root.right)