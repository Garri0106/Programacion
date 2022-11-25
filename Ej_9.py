num = 50
lista = []

def isPrime(num):
    div = 0
    if num >=0:
        for i in range(1, num):
            if num % i ==0:
                div +=1
    if div == 1:
        return True
    else:
        return False


def getPrimeDivisors(num):
    for i in range(1, num):
        if num%i==0 and isPrime(i)==True:
            lista.append(i)
    return lista

print(f"La lista con los divisores primos de {num} es:")
print(getPrimeDivisors(num))
        
    
    
    
    
    
    
    
    
    
