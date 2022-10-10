def prod_or_sum(number1, number2):
    product = number1 * number2
    sum = number1 + number2
    if product >= 1000:
        print(product)
    else:
        print(sum)


# double line after defining object or class otherwise yellow underline hota
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
prod_or_sum(num1, num2)