# Program to compare the first and last items in a given list.

my_list = []

item_count = int(input("Please enter the number of items in list: "))

for each_item in range(item_count):
    item_val = int(input(f"Please enter value {each_item + 1}: "))
    my_list.append(item_val)

print(f"Given list: {my_list}")

if my_list[0] == my_list[-1]:
    print("Result is True")
else:
    print("Result is False")
