n = 3
def main():
    print_square(n)

# create function to print square block
def print_square(size):
    # for each line in _size_ print _#_ * _size_, using for size in range(size) will make the square print incorrectly, will investigate further
    for _ in range(size):
        print_row(size)

# create function to print row of # which # is width or size from square function or n from main to square
# or Abstraction, referring to one by the other
def print_row(width):
    print("#" * width)


# calling main will cause the functions or functions definition within in the function to be called
main()