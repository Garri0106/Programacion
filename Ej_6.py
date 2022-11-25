#num1 = int(input("Introduce un número:"))
num = 23.45

def getNumberOfDigits(num):
    aux = len(str(num))
    for i in (str(num)):
        if i == "." or i == "," or i == "-":
             aux -=1
    return aux

print(getNumberOfDigits(num))









