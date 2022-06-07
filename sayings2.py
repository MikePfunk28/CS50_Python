def main():
    hello("world")
    goodbye("world")
    hello("world")

def goodbye(name):
    print(f"goodbye, {name}")

def hello(name):
    print(f"hello, {name}", end=' ')

# Only run this code if the name of the file, is this, or the
# main file, sayings2.py then run main function, and print the name(main).
if __name__ == '__main__':
    main()
    print(__name__)

print(__name__)