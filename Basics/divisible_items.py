# Ask for a list, the value to divide by and get the divisible items in a separate list.

my_list = []

item_count = int(input("Please enter the number of items in list: "))

for each_item in range(item_count):
    item_val = int(input(f"Please enter value {each_item + 1}: "))
    my_list.append(item_val)

print(my_list)

divisible_by = int(input("Please input the number to check for divisibility: "))
list_of_divisible = []

for item in my_list:
    if item % divisible_by == 0:
        list_of_divisible.append(item)

print(f"{list_of_divisible} is the list of numbers from the original list that are divisible by {divisible_by}.")
