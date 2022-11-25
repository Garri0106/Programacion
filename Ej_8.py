from math import sqrt

a = int(input("Enter the term which will raise to 2:"))
b = int(input("Enter the term which will raise to 1:"))
c = int(input("Enter the independent term:"))

def solveSecondOrderEquation(a, b, c):
    x1 = 0
    x2 = 0
    if ((b**2)-4*a*c) < 0:
      return
    else:
      x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
      x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    return x1, x2

print(f"The solutions to the equation {a}x², {b}x, {c} is:")
print(solveSecondOrderEquation(a, b, c))