#take a three digit no and find its last digit, first digit and reverse it


a=int(input("enter a three digit no"))
last =a%10
print("last_digit", last)

first=a//100
print("first_digit",first)

middle = int((a-(first*100)-last)/10)
print("middle_digit", middle)
print(last*100 + middle*10 +first)

#2nd method
a=456
last =a%10
first_two_digit=a//10
last_of_first_two =first_two_digit%10
first_of_first_two =first_two_digit//10
print(last*100 + last_of_first_two*10 +first_of_first_two)