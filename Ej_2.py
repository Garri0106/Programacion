cadena = "wouhIUGIgYgUYbxswocuOCUWBOUoxbOCWocaoaoOBNC"

def lowCaseInString(cadena):
    c = 0
    for i in cadena:
        if i == i.lower():
            c+=1
        elif i != i.lower():
            c+=0
    return c

print(f"In the string: {cadena};")
print(f"There is a total of {lowCaseInString(cadena)} characters in low case in the string.")