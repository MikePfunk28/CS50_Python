def main():
    x = get_int()
    print(f"x is {x}")

# function get_int() gets no arguments, returns integer.
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
        

main()