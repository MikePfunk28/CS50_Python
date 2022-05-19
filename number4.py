def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            # return int(input("What's x? ")) - could break here and return x, but remove else.
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()