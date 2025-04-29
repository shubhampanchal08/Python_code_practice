#python program to find square root

#way 1: exponentiation

num1=int(input("enter a number"))
sr=num1**(0.5)
print("square root of given number is:",sr)

#way 2:using math module

import math
num=int(input("enter a number: "))
sr=math.sqrt(num)
print("the square root is: ",sr)