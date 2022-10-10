# Adds previous number with current number and outputs it.
# Can modify to iterate through a list of numbers instead of default.

sum_of_nos = 0
previous_no = 0

for number in range(10):
    sum_of_nos = number + previous_no
    print(f"The current number is {number}, the previous number is {previous_no} and their sum is {sum_of_nos}")
    previous_no = number        # when I put this line before print, I was having issue
    sum_of_nos = 0
