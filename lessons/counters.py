"""Practicing Counters"""

num_string: str = "212"
num_string_index: int = 0

num_of_odds: int = 0

while num_string_index < 3:
    if int(num_string[num_string_index]) % 2 == 1:
        num_of_odds +=1
    num_string_index +=1
print(num_of_odds)

age: int = int(input("What is your age?"))
if age <= 12:
    price: int = 5
elif age <= 60:
    price: int = 10
print(price)