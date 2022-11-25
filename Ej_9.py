num=100
lista = []

def isPrime():
    aux = None 
    if num >=0:
        for i in range(2, num):
            if num % i ==0:
                aux == False
            else:
                aux == True
    elif num<0:
        aux == None
isPrime(num)

def getPrimeDivisors(num):
    for i in range(0, num):
        if num%i==0 and isPrime(i)==True:
            lista.append(i)
    return lista

print(f"La lista con los divisores primos de {num} es:")
print(getPrimeDivisors(num))
        
    
    
    
    
    
    
    
    
    