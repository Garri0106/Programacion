num = int(input("Enter a number:"))

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

if isPrime(num) == True:
    print(f"The number {num} is prime")
elif isPrime(num) == False:
    print(f"The number {num} isn't prime")
else:
    print(isPrime(num))
