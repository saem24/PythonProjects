for num in range(1,11):
    for count in range(1,11):
        print(num * count, end=" ")         # end keyword to end with space
    print("\n")

# multiplication table with user input

val = int(input("Input number: "))

for count in range(1,11):
    print(f"{val} x {count} = {val * count}")
