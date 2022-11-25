num1 = int(input("Write the first number (base number):"))
num2 = int(input("Enter the second number (exponent number):"))

def powerIt(num1, num2=0):
    return (num1**num2)

print(powerIt(2))
print(f"The result of raising {num1} to {num2} is {powerIt(num1, num2)}")