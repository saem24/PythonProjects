# Get a new list from existing lists based on condition.
# Can be easily modified to ask the user for the lists as well as the condition.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []

for item in list1:
    if item % 2 != 0:
        new_list.append(item)

for item in list2:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)
