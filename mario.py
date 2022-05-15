n = 3

def main():
    print_column(n)
    print_row(n)
    print_square(n)

def print_column(height):
    for _ in range(height):
        print("#")
#   print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

def print_square(size):
    
    # For each row in square
    for i in range(size):
        
        # For each column or brick in square
        for j in range(size):
        
            # Print brick
            print("#", end="")
        
        # Print call will print the next line in the first loop,
        # Cusor will move to next line by calling print().    
        print()

# calling main will cause the functions within main to be called
main()