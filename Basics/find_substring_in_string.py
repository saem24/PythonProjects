og_string = input("Please input a string: ").lower()
substring = input("Please input the substring you wish to find: ").lower()

# substring_count = 0
# string_as_list = og_string.split(sep=" ")
#
# for string in string_as_list:
#     if string == substring:
#         substring_count += 1
#
# print(f"The substring '{substring}' appears {substring_count} times in the original string.")

print(f"The substring {substring} appears {og_string.count(substring)} times in the original string")

# count() is easier and can find alphabets too as it doesn't depend on making list using single space as separator.
