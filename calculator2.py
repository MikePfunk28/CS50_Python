def main():
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x needs to be an integer")
    # Without the else in the try and except, the print statement would
    # only print if given an integer, but if given a string, it would
    # error UnboundLocalError after still executing the except statement.
    # Could probably break and exit if bad value, but this works as well 
    # and I havent tested the other case.
    else:    
        print("x squared is", square(x))


def square(n):
    return pow(n, 2) # n** 2 or n * n or return pow(n, 2)


if __name__ == "__main__":
    main()