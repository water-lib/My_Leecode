#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
class Solution:
    #求反缀表达式值
    def solve(self , s: str) -> int:
        # write code here
        A=[]
        for i in self.fixin2RPN(s):
            if type(i)==int :#整数直接入栈
                A.append(i)
            else:#遇见其他运算符，则出栈俩个数进行运算
                first = A.pop()
                sec = A.pop()
                if i=="*":
                    res = first*sec
                if i == '/':
                    res = sec/first
                if i =='-':
                    res = sec-first
                if i == '+':
                    res = sec+first
                A.append(res)
        return A[0]
    #中缀转后缀
    def fixin2RPN(self,s):
        por={'(':0,')':0,'+':1,'-':1,'/':2,'*':2,'^':2} #界定优先级
        RPN=[]
        stack_=[]
        num=''
        for i in s:
            if i.isdigit(): #为了出现 100 三个字符组成一个数
                num+=i
            else:
                if num!='':
                    RPN.append(int(num)) #添加100
                num=''
                if i == '(': #左括号直接添加
                    stack_.append(i)
                elif i == ')': #右括号触发出栈，出栈到左括号位置
                    while 1:
                        temp = stack_.pop()
                        if temp != '(':
                            RPN.append(temp)
                        else:
                            break
                elif i in por: #运算符，则比较优先级入栈，栈中优先级大于栈外，则栈中元素放入RPN中，栈外元素入栈
                    if len(stack_)==0:
                        stack_.append(i)
                    else:
                        while 1:
                            #保证栈中有元素,因为始终要和栈顶比较优先值
                            if stack_ and por[i] <= por[stack_[-1]]:
                                RPN.append(stack_.pop())
                            else:        
                                break
                        stack_.append(i)
        if num!="": #多余的num，进行处理
            RPN.append(int(num))
        while stack_: #stack中多余的符号，进行出栈添加到RPN末尾
            RPN.append(stack_.pop())
        return RPN
                