def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

# function get_int(prompt) gets a parameter called, prompt, 
# I can call it whatever I want. returns integer.
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        

main()