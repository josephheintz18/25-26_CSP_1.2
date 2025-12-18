# Method to add numbers
def add_numbers(one, two):
    sum = one + two
    return sum

# Write a method that takes in 3 numbers
# Add the first two, and multiply by the third
# Return the result of the operation
def operation(num1, num2, num3):
    result = (num1 + num2) * num3
    return result

def void_operation(num1, num2, num3):
    result = (num1 + num2) * num3
    print(result)

answer = void_operation(3,4,5)
print(answer)