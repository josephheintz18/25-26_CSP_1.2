
# Make 3 methods following the details given here.
# Method 1: name it "tic" and it takes 2 parameters "num1" and "num2" and returns
# the value of the 2 parameters when subtracted (ie: num1 - num2)
def tic(num1, num2):
    difference = num1 - num2
    return difference

# Method 2: name it "tac" and it takes 1 parameter "exp"
# use a loop to multiply the number 5 by itself "exp" times
# return that value
def tac(exp):
    for j in range(exp):
        product = 5*5
    return product


# Method 3: name it "toe" that takes no parameters.  This method should print
# the results of a method call to "tic(3, 5)" and "toe(4)" to the console
def toe():
    print(tic(3,5))
    print(tac(4))
print(toe())