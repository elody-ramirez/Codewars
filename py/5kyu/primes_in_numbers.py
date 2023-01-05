# Given a positive number n > 1 find the prime factor decomposition of n.
#The result will be a string with the following form :

 #"(p1**n1)(p2**n2)...(pk**nk)"

#where a ** b means a to the power of b
#with the p(i) in increasing order and n(i) empty if n(i) is 1.

#Example: n = 86240 should return "(2**5)(5)(7**2)(11)" */

def prime_factors(n):
    result = ""
    i = 1
    while n > 1:
        i += 1
        count = 0
        while n % i == 0:
            n /= i
            count += 1
        if count > 0:
            result += "("+str(i)+"**"+str(count)+")"
    result = result.replace("**1","")
    return result

print(prime_factors(7775460)) #(2**2)(3**3)(5)(7)(11**2)(17)
