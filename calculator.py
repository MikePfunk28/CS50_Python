x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

#z = round(x + y)
# will concatinate the string because of the plus, and keyboard always returns text so you 
# need to convert it to type int
#z = int(x) + int(y)

print(f"{z:.2f}")

#print(f"{z:,}")

#print(z)