'''
Sharad: test whether a number is prime. Use this
function to find the number of prime numbers less than 10,000
'''
def isPrime(lnum):
    divisor =2
    while divisor <= lnum/2:
        if lnum %divisor==0:
            return False ## return false saying that it is not a prime number        
        divisor += 1
    return True   ### if no number which divides the input then it is prime 
        
        
def main():
    cnt=0
    for i in range(2,10000):
        if isPrime(i):
            print("\t"+str(i), end =' ')
            cnt +=1
            if cnt%10 == 0:
                print()
    print ("\ntotal number of primes:", cnt )

main()