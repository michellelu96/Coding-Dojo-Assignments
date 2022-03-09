/*String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

  /*const str1 = "a x a";
  const expected1 = true;
  
  const str2 = "racecar";
  const expected2 = true;
  
  const str3 = "Dud";
  const expected3 = false;
  
  const str4 = "oho!";
  const expected4 = false;
  
  /*
   * - create a function
   * - create 2 for loops
   * - create a variable
   * - iterate through string comparing first and last index then move inward
   * 
   * 
   * * */ 


  /**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */

  /* function isPalindrome(str){
    for(var left=0; left<str.length/2; left++) {
        var right = str.length-1-left;
        if(str[left] != str[right]) {
            return false;
        }
    }
    return true;
  }
  
  console.log(isPalindrome(str1))
  */

//const { isPalindrome } = require("./isPalindrome");
const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

const str4 = "a1001x20002y5677765z";
const expected4 = "5677765";

const str5 = "a1001x20002y567765z";
const expected5 = "567765";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
 
function longestPalindromicSubstring(str) {
    var longest="";

    var getLongest = function(left,right){
        while(left>=0 && right <str.length&&string[left]==string[right])
        left--;
        right++;

    if(right - left > longest.length){
        longest=str.slice(left+1,right);
        }
    }

    for(var i = 0;i<str.length;i++){
        getLongest(i,i+1);
        getLongest(i,i)
        if((str.length-1)*2 < longest.length){
            break;
        }
    }
    return longestPal
}

console.log(longestPalindromicSubstring(str1))

module.exports = { longestPalindromicSubstring: longestPal };