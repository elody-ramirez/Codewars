'use strict'

/* Your job is to write a function which increments a string, to create a new
string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the
new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be
considered.*/

function incrementString (strng) {
  // First pull just the word
  const onlyWord = strng.replace(/\d+/g, '')
  // Second pull just the number
  let num = strng.slice(onlyWord.length) || "0"
  // then get the length of the number to be used to fill in 0s if necessary
  const numbersLength = strng.length  - onlyWord.length
  // Next lines, converts to int, increments 1 and then back to string
  num = parseInt(num)
  num++
  num = num.toString()
  // fills in 0s if needed
  while (num.length < numbersLength) {
    num = "0" + num
  }
  return onlyWord + num
}

console.log(incrementString("foobar000")) // "foobar001"
console.log(incrementString("foo")) // "foo1"
console.log(incrementString("fooobar001")) // "foobar002"
console.log(incrementString("foobar99")) // "foobar100"
console.log(incrementString("foobar099")) // "foobar100"
console.log(incrementString("")) // "1"
