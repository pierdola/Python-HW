class Stack:
    def __init__(self, s1, s2): # Инициализируем
     self.s1 = s1
     self.s2 = s2
     
     def v(self): # Функция слияния
        s3=s1+s2 
        return s3 

s1=[5,8,9,4,6,8]
s2=[4,8,9,7,6,2,3]
stack = Stack(s1, s2)
print(stack.v())

   




