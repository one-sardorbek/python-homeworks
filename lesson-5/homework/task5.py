def is_prime(n):
    a=True
    for i in range(2,int(n**(1/2))):
        if n%i==0:
            a=False
            break
    return a
n=int(input())
print(is_prime(n))