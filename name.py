import sys

# Best way to implement this
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)# can use any word, for arg.



# Probably the worst way to do this below
if len(sys.argv) < 2:
    print("Too few arguements")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, My name is", sys.argv[1])



# Better way to write the same code.
# Check for errors
if len(sys.argv) < 2:
    sys.exit("too few arguements") # too few and it will exit without the last print on 21
elif len(sys.argv) > 2:
    sys.exit("too many arguments") # too many and it exits without printing line 21


# Print name tags
print("hello, my Name is", sys.argv[1])

print(sys.argv[0], sys.argv[1])