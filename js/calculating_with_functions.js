/* This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations:
plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function
represents the right operand
Divison should be integer division. For example, this should return 2, not
2.666666...:

eight(dividedBy(three()));
*/
//helper function
function checkfunc(num, func) {
  if (!func) {
    return num
  }
  return func(num)
}

function zero(func) { return checkfunc(0, func) }
function one(func) { return checkfunc(1, func) }
function two(func) { return checkfunc(2, func) }
function three(func) { return checkfunc(3, func) }
function four(func) { return checkfunc(4, func) }
function five(func) { return checkfunc(5, func) }
function six(func) { return checkfunc(6, func) }
function seven(func) { return checkfunc(7, func) }
function eight(func) { return checkfunc(8, func) }
function nine(func) { return checkfunc(9, func) }

function plus(x) {
  return function(y) {
    return y + x;
	}
}
function minus(x) {
  return function(y) {
		return y - x;
	}
}
function times(x) {
  return function(y) {
    return y * x;
  }
}
function dividedBy(x) {
  return function(y) {
		return Math.floor(y / x);
	}
}

console.log(seven(times(five()))) // 35
console.log(four(plus(nine()))) // 13
console.log(eight(minus(three()))) // 5
console.log(six(dividedBy(two()))) // 3
