def main():
    x = int(input("what's x? ")) # function is_even() takes a number,
    if is_even(x):               # n and uses mod to determine even or odd
        print("Even")
    else:
        print("Odd")

# is_even(n) takes user input x as it takes n, above we pass x into is_even(x)
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


#main()