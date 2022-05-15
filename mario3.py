n = 3


def print_column(height):
    for _ in range(height):
        print("#")
#   print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

# create function to print square block
def print_square(size):
    # for each line in _size_ print _#_ * _size_, using for size in range(size) will make the square print incorrectly, will investigate further
    for _ in range(size):
        print("#" * size)

# calling main will cause the functions or functions definition within in the function to be called
#main()
print_column(n)
print_row(n)
print_square(n)