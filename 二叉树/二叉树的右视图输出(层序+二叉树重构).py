#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 求二叉树的右视图
# @param xianxu int整型一维数组 先序遍历
# @param zhongxu int整型一维数组 中序遍历
# @return int整型一维数组
#
from collections import deque
class Solution:
    def solve(self , xianxu: List[int], zhongxu: List[int]) -> List[int]:
        # write code here
        A = self.fun(xianxu,zhongxu)
        results = []
        dq = deque([A]) #deque需要迭代对象。A是root的首地址，root是不可迭代对象，因此必须进行转换。
        while dq:
            res = []    
            for _ in range(len(dq)):
                cur = dq.popleft()
                res.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            results.append(res.pop())#层次遍历，每次取结果最右边，pop()或者[-1]
        return results
    def fun(self,xianxu,zhongxu): #进行层次遍历
        if len(xianxu)==0 or len(zhongxu)==0:
            return None
        root_val = xianxu[0]
        root_ = TreeNode(root_val)
        idx = zhongxu.index(root_val)
        root_.left = self.fun(xianxu[1:idx+1], zhongxu[:idx])
        root_.right = self.fun(xianxu[idx+1:], zhongxu[idx+1:])
        return root_