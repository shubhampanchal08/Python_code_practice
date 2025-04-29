#swap two variable's:

#way 1: using third variable

x=float(input("enter the first variable :"))
y=float(input("enter the second variable :"))

temp=x
print("temp:",temp)
x=y
y=temp

print("value of x :",x , "and value of y :",y)


#way 2: without using third variable
x=float(input("enter the x variable :"))
y=float(input("enter the y variable :"))
x,y=y,x
print("value of x :",x , "and value of y :",y)
