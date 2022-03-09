/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 function binarySearch(sortedNums, searchNum) {
     var mid = Math.floor(sortedNums.length/2);
     var newarr = [];
     if (sortedNums.length < 1){
         return false
        }
        if (sortedNums == 1 && sortedNums != searchNum){
            return false
        }
        
        if(searchNum == sortedNums[mid]){
            return true;
        }else if(searchNum < sortedNums[mid]){
            newarr = sortedNums.slice(0,mid)
            return binarySearch(newarr,searchNum)
        }else if(searchNum > sortedNums[mid]){
            newarr = arr.slice(mid+1,sortedNums.length)
            return binarySearch(newarr,searchNum)
        }
    }
    */
    function binarySearch(sortedNums, searchNum) {
        var mid = Math.floor(sortedNums.length/2);
        if (sortedNums.length < 1){
            return false
        }
        if (sortedNums == 1 && sortedNums != searchNum){
            return false
        }
        if(searchNum == sortedNums[mid]){
            return true;
        }else if(searchNum < sortedNums[mid]){
            return binarySearch(sortedNums.slice(0,mid),searchNum)
        }else if(searchNum > sortedNums[mid]){
            return binarySearch(sortedNums.slice(mid+1,sortedNums.length),searchNum)
        }
    }

console.log(binarySearch(nums3,searchNum3))

module.exports = { binarySearch };

/*****************************************************************************/

/* 
  Recursively reverse a string
  helpful methods:
  str.slice(beginIndex[, endIndex])
  returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
function reverseStr(str) {}

module.exports = { reverseStr };

/*****************************************************************************/