og_word = input("Input any word: ")
chars_to_remove = int(input("Enter number for characters to be removed: "))
direction = input("Enter 'L' to remove from left and 'R' to remove from right: ").upper()
final_word = ""

if direction == "L":
    for char in og_word[chars_to_remove:]:
        final_word += char
elif direction == "R":
    for char in og_word[:len(og_word) - chars_to_remove]:
        final_word += char
print(final_word)
