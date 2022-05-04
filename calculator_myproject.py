x = float(input("What's x? "))
y = float(input("What's y? "))
oper = input("What type of operation? add, sub, mul, div ")
if oper == "add":
    print(x + y)
elif oper == "sub":
    print(x - y)
elif oper == "mul":
    print(x * y)
elif oper == "div":
    print(x / y)
# will concatinate the string because of the plus, and keyboard always returns text so you 
# need to convert it to type int
#z = int(x) + int(y)
print(x + y)
#print(z)