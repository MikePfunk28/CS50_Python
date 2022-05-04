def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function,")
    return wrapper
# hello functions is wrapped in annouce decorator that gives us
# a warning then runs the fuctions then prints done with the
# fucntion.
@announce
def hello():
    print("Hello, world!")

hello()
