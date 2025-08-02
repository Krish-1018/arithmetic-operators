#take a four digit number and find the sum of its digits

a = int(input("enter the number"))

first = a//1000
last = a%10
second = (a//100)%10
third = (a//10)%10 

print(first + second + third + last)