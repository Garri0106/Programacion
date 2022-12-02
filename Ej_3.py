cadena = "wouhIUGIgYgUYbxswocuOCUWBOUoxbOCWocaoaoOBNC"

def upperCaseInString(cadena):
    c = 0
    for i in cadena:
        if i == i.upper():
            c+=1
        elif i != i.upper():
            c+=0
    return c

print(f"In the string: {cadena};")
print(f"There is a total of {upperCaseInString(cadena)} characters in upper case in the string.")