'''
Created on Nov 22, 2022

@author: estudiante
'''
n = int(input("Introduce un número:"))
def computeFactorial():
    if n >=0:
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return fact
    else:
        return None
print(f"El factorial es {n}!={computeFactorial()}")