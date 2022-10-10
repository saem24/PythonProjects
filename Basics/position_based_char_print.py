# Prints characters based on their even or odd position in a string.

input_str = input("Please input the string: ")
is_even = input("'True' for even and 'False' for odd: ").lower()
val_type = ""

for char in range(0, len(input_str), 2):
    if is_even == "true":
        val_type = "even"
        print(input_str[char])
    elif is_even == "false":
        val_type = "odd"
        print(input_str[char + 1])

print(f"Original string is {input_str} and only {val_type} characters are being printed")
