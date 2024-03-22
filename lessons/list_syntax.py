"""Demonstrate Basic List Syntax"""

# Create an empty list
grocery_list: list[str] = list () # <- constructor
grocery_list: list[str] = [] # <- literal
print("Empty list: ")
print(grocery_list)

# Add to the list
grocery_list.append("milk")
grocery_list.append("pizza")
grocery_list.append("frosted flakes")
print("After adding things: ")
print(grocery_list)

# Create a list with objects in it
grocery_list2: list[str] = ["milk", 'pizza', "frosted flakes"]
print("Already populated list: ")
print(grocery_list2)

grocery_list2.append("whipped cream")
print("Add another thing")
print(grocery_list2)

# Indexing
print("Printing one item: ")
print(grocery_list[1])

# Modifying by Index
x: list[str] = ["c", "a", "r", "s"]
x[2] = "t"
print(x)

grocery_list[0] = "pretzels"
print("Modifying: ")
print(grocery_list)

# Length of a list
print("Length: ")
print(len(grocery_list))

# Removing an item 
print("Removing: ")
grocery_list.pop(2)
print(grocery_list)

# Creating a function
print("Function!!")
def display(my_list: list[str]) -> None:
    print(my_list)

display(grocery_list)
x = display(["Anusha", "Jack", "Vrinda"])
print(x) # gives an output of none


def create(x: str, y: str) -> list[str]:
    new_list: list[str] = [x, y]
    return new_list

print(create("Hello", "World")) # have to print out the return value
x: list[str] = create("a", "b")
print(x)