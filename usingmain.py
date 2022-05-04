def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

# Nothing happens until you call the function below then it does
# what the function should do.
main()