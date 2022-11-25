num = int(input("Enter a number:"))

def isPrime(num):
    if num >=0:
        for i in range(2, num):
            if num % i ==0:
                return False
            else:
                return True
    if num<0:
        return None
if isPrime(num) == True:
    print(f"The number {num} is prime")
elif isPrime(num) == False:
    print(f"The number {num} is'nt prime")
else:
    print(isPrime(num))