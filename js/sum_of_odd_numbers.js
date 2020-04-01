'use strict'

/* Given the triangle of consecutive odd numbers:

             1                            = 1
          3     5                         = 8
       7     9    11                      = 27
   13    15    17    19                   = 64
21    23    25    27    29                = 125
...                                       = 216
Calculate the row sums of this triangle from the row index (starting at index 1)*/

function rowSumOddNumbers(n) {
  // The sum of each row is the cube of the row number
	return n**3
}

console.log(rowSumOddNumbers(1))
console.log(rowSumOddNumbers(42))
