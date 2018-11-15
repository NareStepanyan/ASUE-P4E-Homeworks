num = int(input("Enter positive integer: "))
def prime(number):
    primes = []
    for i in range(2, number + 1):
        isPrime = True
        for num in range(2, i):
            if i % num == 0:
                isPrime = False
        
        if isPrime:
            primes.append(i)
    return primes
print(prime(num))


    
    
