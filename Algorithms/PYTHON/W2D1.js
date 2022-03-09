/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.

 function frequencyTableBuilder(arr) {
    var result = {};
    var count = 1;
    for(var i=0; i < arr.length; i++){
        if(arr[i] != arr[i+1]){
            result[i] = arr[i]
        }else if (arr[i]==arr[i])


    }
}

function frequencyTableBuilder(arr) {
    var result = {};
    var count = 1;
    for(var i=0; i < arr.length; i++){
        for(var j = 1; j < arr.length; j++){
            if(arr[i] == arr[i+j]){
                var key = arr[i]
                result[key]=count
                count++
     


    }
}
    return result
}
*/
function frequencyTableBuilder(arr) {
    result = {}
    for (var i = 0; i < arr.length; i++) {
        if (!result[arr[i]])
            result[arr[i]] = 0;
        result[arr[i]]++;
    }
    return result
}
console.log(frequencyTableBuilder(arr2))

module.exports = { frequencyTableBuilder };

/*****************************************************************************/


// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

/*
*
*/
function oddOccurrencesInArray(nums) {
    result = {}
    for (var i = 0; i < nums.length; i++) {
        if (!result[nums[i]]){
            result[nums[i]] = 0;
        result[nums[i]]++;
    }
    for (var x = 0; i < result.length; i++) {
        if (result[nums[x]]%2 != 0){
            console.log(result[nums])
        }
    }
}

    return result
}

console.log(oddOccurrencesInArray(nums2))

/*****************************************************************************/
