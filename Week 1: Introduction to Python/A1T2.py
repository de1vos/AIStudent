# Task 2: Loops and Conditionals
# List of contact names
contacts = ["John Smith", "Bob Boulder", "Anna Song"]

# Display welcome message for each contact
# Remember, special message for names starting with 'A'
for name in contacts:
    if (name.startswith("A")):
        print("Welcome " + name + "! A very special welcome to you, indeed!")
    else:
        print("Welcome " + name + "!")