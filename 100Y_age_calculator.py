# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name= input("whats your name: ")
age=int(input("whats your age: "))
year=str((2014-age)+100)
print(name + "will 100 years old in the year :"+year)