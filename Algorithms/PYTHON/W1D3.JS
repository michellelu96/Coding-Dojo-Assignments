// write function
// for loops?
//make a new string
//push stuff into a new string
// make a loop for if final string is not shorter than the orignal string return it
//return it

/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */
  const str1 = "aaaabbcddd";
  const expected1 = "a4b2c1d3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs only if the
   * character occurs more than two time.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */


  //write function
  //a for loop
  //a new variable for new string
  //make a if loop to check if final result is the same length as original

  function encodeStr(str) {
    var result = "";
    var count = 1;
    for (var i =0; i < str.length; i++){
          if(str[i]==str[i+1]){
              count++;
          }
          else{
              result+=str[i] + count;
              count = 1;
          }
      }
      if (result.length >= str.length){
          return str
      }
    return result
}
console.log(encodeStr(str3))
module.exports = { encodeStr };
/* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {}

module.exports = { decodeStr };

/*****************************************************************************/
