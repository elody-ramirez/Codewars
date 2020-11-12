# Given a positive number n > 1 find the prime factor decomposition of n.
#The result will be a string with the following form :

 #"(p1**n1)(p2**n2)...(pk**nk)"

#where a ** b means a to the power of b
#with the p(i) in increasing order and n(i) empty if n(i) is 1.

#Example: n = 86240 should return "(2**5)(5)(7**2)(11)" */

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
             n //= i
             factors.append(i)
    if n > 1:
        factors.append(n)
    this_dict = list_to_dict(factors)
    return dict_to_string(this_dict)

def list_to_dict(lst):
    dict = {}
    for i in lst:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def dict_to_string(d):
    result = ''
    for key in d:
        if d[key] > 1:
            result += '('+str(key)+'**'+str(d[key])+')'
        else:
            result += '('+str(key)+')'
    return result


print(prime_factors(7775460)) #(2**2)(3**3)(5)(7)(11**2)(17)
