chain = "cadenaqwhibcowibsacijwkcejhbsbxvjzhrfiuepqwljksdkñahcweocby"
print(f"The chain is: {chain}")
character = str(input("Enter the character to see how many times it repeates:"))
while character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9":
    character = str(input("Enter a valid character (not a number):"))
while len(character) != 1:
    character = str(input("Enter only one character:"))


def characterInString(chain):
    return chain.count(character)

print(f"The character {character} is a total of {characterInString(chain)} times")

#He conseguido hacerlo con la función .count pero te pongo un intento que he hecho pero no he conseguido terminar
#(def characterInString(chain):
#    c = 0
#    for i in chain:
#        while i == chain[i]:
#            c += 1
#    return c)
#Tras corregirlo en clase he visto que es asi:
#    c = 0
#    for i in chain.upper:
#        if i.upper == character:
#            c += 1
#    return c