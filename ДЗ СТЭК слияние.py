class Stack:
    def __init__(self, Stack): # Инициализируем
     self.s1 = Stack
     self.s2 = Stack
     
     
    def push(self, elem): # Функция добалвения ТОЛЬКО ДЛЯ С1
       self.s1.append(elem)
       return self.s1
    
    def pop(self): # Функция удаления ТОЛЬКО ДЛЯ ЭЛЕМЕНТОВ С2
        self.s2.pop()
        return self.s2

    def v(self): # Функция слияния
        s1.push(s2.pop()) #Добавляем в С1 удалённые элементы С2
        return self.s1 #Возвращаем значение С1

    

   




