def main():
    number = get_number()
    meow(number) 

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n # can _break_ but then need to _return n_ outside the loop,
                     # but inside the fuction def get_number()

def meow(n):
    for _ in range(n):
        print("meow")

main()