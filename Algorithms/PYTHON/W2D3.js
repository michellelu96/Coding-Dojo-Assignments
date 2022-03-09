const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */

/**
 * make function
 * make 2 count variable
 * use a for loop
 * check for both parenteses seperately
 * add to count
 * use modulus to check if it's even
 * return the result
 
function parensValid(str) {
    var count =0;
    var count1=0;
    for(var i=0;i<str.length;i++){
        if (str[i]=='(') {
            count++
        }else if(str[i]==')'){
            count1++
        }
    }
    if (count==count1){
        return true
    }else {
        return false
    }
}

function parensValid(str) {
  var start = "(";
    var end = ")"

   for (var i = 0; i < str.length; i++) {
     if (str[i] == start) {
           if (str[str.length - i] == end){
               return true
           }
       }

       if (str[i] != start || end) {
          
     }
   }
  return false
}
*/

function parensValid(str) {
    var count =[];
    for(var left=0;left<str.length/2;left++){
        var right = str.length-1-left;
        if(str[left]=='('){
            count.push(str[left]);
            for(var right = str.length-1-left;right>str.length/2;right--){
                if(str[right]==')'){
                    count.push(str[right]);
                }
            }
        }
        console.log(count)
    }
}



console.log(parensValid(str1));



module.exports = { parensValid };

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {}

module.exports = { bracesValid };