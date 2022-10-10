# Code to print different kinds of patterns

for i in range(6):
    for j in range(i):
        print(i, end=" ")
    print("\n")


for i in range(6):
    for j in range(i):
        print(j + 1, end=" ")       # +1 because otherwise it starts with 0.
    print("\n")


print("\n")


for i in range(5, 0, -1):           # can use start, stop, step with range to reverse things.
    for j in reversed(range(i)):    # can use reversed() to reverse things.
        print(j + 1, end=" ")
    print("\n")
print("\n")


for i in range(6):
    for j in range(i):
        print(j + 1, end=" ")
    print("\n")
for i in reversed(range(6)):
    for j in range(i - 1):          # -1 because I didn't want 12345 to repeat twice so I had it skip one step.
        print(j + 1, end=" ")
    print("\n")


for i in range(6):
    print(i * "* ")


for i in range(6,0,-1):
    for j in range(0,i):
        print("*", end=" ")
    print("\t\t")                   # \t doesn't add new line but tabs to different line.
