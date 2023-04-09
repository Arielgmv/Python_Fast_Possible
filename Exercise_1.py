# Exercise 1: Calculate the multiplication and sum of two numbers

"""
number_one = int(input('First Number: '))
number_two = int(input('Second Number: '))

multiplication = number_one * number_two
sum = number_one + number_two

if multiplication <= 1000:
    print('The result is ', multiplication)
else:
    print('The result is ', sum)
"""
def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <=1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print('The result is ', result)

# second condition
result = multiplication_or_sum(40, 30)
print('The result is ', result)