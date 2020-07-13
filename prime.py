def prime_function(num):
    isprime=True
    for i in range(2,num):
        if num%i==0:
            isprime=False
    if isprime==True:
        return ("PRIME")
    else:
        return ("not prime")

              