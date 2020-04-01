'use strict'
/* You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their
places.

Zero isn't an odd number and you don't need to move it. If you have an empty
array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4] */

function sortArray(array) {
  if (array.length > 1) {
    const odds = []
    for (let i = 0; i < array.length; i++) {
      if (array[i] % 2 !== 0){
        odds.push(array[i])
      }
    }
    let sorted = false
    // while(!sorted) {
    //   sorted = true
    //   for(var i = 0; i < odds.length; i++) {
    //     if(odds[i] < odds[i - 1]) {
    //       let temp = odds[i];
    //       odds[i] = odds[i - 1];
    //       odds[i - 1] = temp;
    //       sorted = false;
    //     }
    //   }
    // }
    odds.sort((a,b) => a - b)
    let oddscount = 0
    for (let i = 0; i < array.length; i++) {
      if (array[i] % 2 !== 0){
        array[i] = odds[oddscount]
        oddscount++
      }
    }
    return array
  } else {
    return array
  }
}

console.log(sortArray([5, 3, 2, 8, 1, 4])) // [1, 3, 2, 8, 5, 4]
console.log(sortArray([5, 3, 1, 8, 0])) // [1, 3, 5, 8, 0]
console.log(sortArray([])) // []
