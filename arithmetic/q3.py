# Take two numbers a and b. and find the integer and decimal part when a is divided by b

a = int(input("enter first number"))
b= int(input("enter second number"))

#for integer part

integer_part = a//b  #or int(a/b)
print(integer_part)

#for decimal part

div = a/b
decimal_part = div - integer_part
print(decimal_part)



