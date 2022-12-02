cadena = "Bocadillo02837de2chope7"

def numberInString(cadena):
    c = 0
    for i in cadena:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i =="9":
            c+=1
        elif i != int:
            c+=0
    return c

print(f"In the chain: {cadena};")
print(f"There's a total of {numberInString(cadena)} number(s).")