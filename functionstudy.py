
def greet():
    print("Hello, world!")
    return "HELLLLO"            # stores the value "HELLLLO" in function
    pass                        # placeholder - allows function to be empty - not relevant here

greet()             # only gives print
print(greet())      # gives full funct.

def greetname(first_name, last_name):
    print("Hello", first_name, last_name)
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

greetname(first_name, last_name)

def default_greet(friend = "friend"):   # = gives a defualt value when not specified
    print("Hello", friend)
default_greet()
default_greet("ruby") # overwrites default