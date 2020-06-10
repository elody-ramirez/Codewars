/* Complete the solution so that the function will break up camel casing, using
a space between words. */

// complete the function
function solution(string) {
  return(string.replace(/([A-Z])/g, ' $1'));
}

// complete the function
function solution2(string) {
  let answer = ""
  for (let i = 0; i < string.length; i++){
    if (string[i] === string[i].toUpperCase()) {
      answer+= " "
      answer+= string[i]
    } else {
      answer+= string[i]
    }
  }
  return answer
}

console.log(solution('camelCasing'))
console.log(solution('camelCasingTest'))
