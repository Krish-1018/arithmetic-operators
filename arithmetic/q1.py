#program to calculate simple interest and compound interest 


p =  int(input("Enter Principle "))
r = int(input("Enter Rate of Interest "))
t = int(input("Enter Time "))

si = p*r*t/100

# p(1+r/100)^t
amt = p*(1+r/100)**t
ci = amt - p 

print(si, ci)