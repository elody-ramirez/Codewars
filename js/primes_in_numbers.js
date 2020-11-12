/* Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"

where a ** b means a to the power of b
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)" */

function primeFactors(n){
  let result = ""
  let i = 1
  while (n > 1) {
    i += 1
    let count = 0
    while (n % i == 0){
      n /= i
      count += 1
    }
    if (count > 0) {
      result += "("+i+"**"+count+")"
    }
  }
  result = result.replace("**1","")
  return result
}

console.log(primeFactors(7775460)) // (2**2)(3**3)(5)(7)(11**2)(17)
