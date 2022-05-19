while True:
    try:
        x = int(input("What's x? "))
        # break - could break here and print below but remove else.
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")