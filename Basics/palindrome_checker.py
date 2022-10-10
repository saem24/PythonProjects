og_no = int(input("Please enter a number: "))
new_no = og_no
rev_no = 0

while new_no > 0:
    remainder = new_no % 10                 # gets last digit as remainder from original number
    rev_no = (rev_no * 10) + remainder      # puts that last digit as first digit for making reversed number
    new_no = new_no // 10                   # deletes the last digit from the original number

if og_no == rev_no:
    print(f"{og_no} is a palindrome")
else:
    print(f"{og_no} is not a palindrome")
