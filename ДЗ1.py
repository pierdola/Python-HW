class Student():
    def __init__(self, name, lname, age, gender, ind):
        self.name=name
        self.lname=lname
        self.age=age
        self.gender= gender
        self.ind=ind
student1= Student('Сavid', 'Usmelizade', 17, 'm', 1044)
student2= Student('Anna','Grishina', 18, 'w', 1109)
student3= Student('Anton','Gorbunov', 23, 'm ', 1908)
student4= Student('Davron','Canvoy', 18, 'm', 8777)
student5= Student('Polina','Usherzon', 19, 'm', 4126)
students=[student1, student2, student3, student4, student5]

1 задание

for l in range(len(students)):
    print(students[l].name, students[l].lname)

2 задание

a=[]
for k in range(len(students)):
    a.append(students[k].age)
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1]=a[j+1], a[j]
print(a)
[17, 18, 18, 19, 23]
3 задание

def bin(a, x):
    left=0
    right=len(a)-1
    while left<=right:
        middle= (left+right)//2
        if x==a[middle]:
            return middle
        elif x>a[middle]:
            left=middle+1
        elif x<a[middle]:
            right=middle-1
    return -1
x=int(input())
result= bin(a, x)
if result==-1:
    print('element ne naiden')
else:
    print(students[result].name, students[result].lname)





def bin(a, x):
    left=0
    right=len(a)-1
    while left<=right:
        middle= (left+right)//2
        if x>a[middle]:
            left=middle+1
        else:
            right=middle-1
    if a[left]==x:
        return left
    return -1

x=int(input())
result= bin(a, x)
if result==-1:
    print('studenta takogo vozrasta net')
else:
    print(students[result].name, students[result].lname)
