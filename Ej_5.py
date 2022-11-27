num1 = int(input("Enter the first number (base number):"))
num2 = int(input("Enter the second number (exponent number):") or 0)

def powerIt(num1, num2): 
    if num1<0 or num2<0:
        return (-num1**(num2))
    elif num1 == 0:
        return 0
    elif num2 == 0:
        return  1
    else:
        return (num1**num2)
print(f"The result of raising {num1} to {num2} is {powerIt(num1, num2)}")