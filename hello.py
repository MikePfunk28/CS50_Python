# Ask user for their name (Last step do it all together, remove space and capitalize each word)
name = input("What's your name? ").strip().title()

# Remove whitespace from str
# name = name.strip()

#Capitalize user's name title does each word
# name = name.title()

# Remove whitespace from str and capitalize each word
# name = name.strip().title()

# Say Hello to user (the comma allows you to pass multiple arguments and adds a space for you
# so you do not need to add your own space)
# print("Hello, " + name)
# print("Hello,",name)
print(f"Hello, {name}") #f formats a string when using curly brackets
# Example on how to use quotes
# print("Hello, \"friend\"")

# print the main file
#print(__name__)