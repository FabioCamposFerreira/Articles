#Um gerador de números primos

def gen_primes():
    primes=[]
    i = 1
    while i<100:
        i += 1
        answer = 1
        for p in range(1,i):
            j = i % p
            if j == 0:
                answer = 0
        if answer == 1:
            yield i




print(list(gen_primes()))