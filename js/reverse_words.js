'use strict'

/* Complete the function that accepts a string parameter, and reverses each word
in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps" */

function reverseWords(str) {
  /* First split/reverse/join flips every character
  Second split/reverse/join flips every word so that the first word is back
  in the first spot but with the characters reversed*/
  return str.split('').reverse().join('').split(' ').reverse().join(' ')
}

// 'ehT kciuq nworb xof spmuj revo eht yzal .god'
console.log(reverseWords('The quick brown fox jumps over the lazy dog.'))
console.log(reverseWords('apple')) // 'elppa'
console.log(reverseWords('a b c d')) // 'a b c d'
console.log(reverseWords('double  spaced  words')) // 'elbuod  decaps  sdrow'
