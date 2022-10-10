def exponent(base, exp):
    val = 1
    for count in range(0, exp):
        val = val * base
    return val


base_val = int(input("Please input base value: "))
exp_val = int(input("Please input exponent value: "))
final_val = exponent(base_val, exp_val)
print(f"{base_val} raised to the power of {exp_val} is {final_val}.")
