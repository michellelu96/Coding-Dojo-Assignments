/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/
 

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

// bonus test case
const str3 = "abcdeab"
const expected3 = "cdeab"


/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
 function stringDedupe(str){
    var str2 = ""
    for(var x = 0; x < str.length; x++){
        if (str2.includes(str[x])){
        }
        else {
            str2 += str[x]
        }
    }
    return str2
  }


module.exports = { stringDedupe };


// -----------------------------------------------------------------------


/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */

/**
 * write function
 * write a for loop going down then put in new string
 * check for spaces
 * return new string
 */
function reverseWords(str) {
    var string1 = "";
    for(var i = str.length - 1; i >= 0; i--){
        if(str[i]!= " "){
            string1+=str[i]
        }
        if(str[string1.length] == " "){
            string1 += str[string1.length];
    }

}
return string1
}

console.log(reverseWords(str3))
module.exports = { reverseWords };


// -----------------------------------------------------------------------


/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
const expected1 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) {}

module.exports = { reverseWordOrder };