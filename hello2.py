def hello(to="world"): # you can set a function equaled to by using, def hello(to="world"):
    print("hello,", to)
# What happens here is when hello(name) is called
# the program will asssume hello(to) and it will
# print("hello,", to) assuming to is (name)

# Used our function in two ways
hello()
name = input("What's your name? ")
hello(name)