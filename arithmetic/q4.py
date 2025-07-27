#take a two digit no and find its last digit, first digit and reverse it

# for last digit
a = int(input("enter a two digit no"))
last_digit = a%10
print("last_digit", last_digit)

# for first digit
first_digit= (a -last_digit)//10 # or a//10 or int(a/10)
print("first_digit", first_digit)

#reverse the two digit no 

# these are not correct methods
# print(last_digit,first_digit, sep="")
# print(last_digit, end="")
# print(first_digit)
# print(f"{last_digit}{first_digit}")

# this approach is correct
print(last_digit*10 + first_digit)