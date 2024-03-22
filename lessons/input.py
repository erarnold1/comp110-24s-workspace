"""Practice with variables & input function"""

first_name: str = input("What is your name? ")
fav_num_str: str = input("What is your favorite number ")
fav_num: int = int(fav_num_str)
higher_num: int = (fav_num + 1)

print("Hello " + first_name + "!")
print("My favorite number is " + str(higher_num))
