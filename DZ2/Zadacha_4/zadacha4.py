# Задайте список из N элементов, заполненных числами из промежутка [-N, N].


y=int(input("Введите число --> "))
x=y*(-1)
list=[]
while y != x:
    list.append(x)
    x +=1
list.append(x)
print(list)
