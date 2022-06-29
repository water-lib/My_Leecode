# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return bool布尔型
#
class Solution:
    def isSymmetrical(self , pRoot: TreeNode) -> bool:
        # write code here
        #迭代手法 栈
        if not pRoot:
            return True
        A=[]
        A.append(pRoot.left)
        A.append(pRoot.right)
        while A:
            right = A.pop()
            left = A.pop()
            if left==None and right==None:
                continue
            if right==None or left==None or left.val != right.val:
                return False
            A.append(left.left)
            A.append(right.right)
            A.append(left.right)
            A.append(right.left)
        return True
            
        
        
        
#         if not pRoot: #递归手法
#             return True
#         return self.fun(pRoot.left, pRoot.right)
#     #递归一般有俩个函数
#     def fun(self,left,right):
#         if left==None and right!=None:return False
#         if left==None and right!=None:return False
#         if left== None and right==None:return True
#         if left.val!=right.val:return False
#         out = self.fun(left.left, right.right)
#         in_ = self.fun(left.right, right.left)
#         return out and in_
        
        
        