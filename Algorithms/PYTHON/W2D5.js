/* 
  Given an array of objects / dictionaries to represent new inventory,
  and an array of objects / dictionaries to represent current inventory,
  update the quantities of the current inventory
  
  if the item doesn't exist in current inventory, add it to the inventory
  return the current inventory after updating it.
*/

const newInv1 = [
    { name: "Grain of Rice", quantity: 9000 },
    { name: "Peanut Butter", quantity: 50 },
    { name: "Royal Jelly", quantity: 20 },
];
const currInv1 = [
    { name: "Peanut Butter", quantity: 20 },
    { name: "Grain of Rice", quantity: 1 },
];
const expected1 = [
    { name: "Peanut Butter", quantity: 70 },
    { name: "Grain of Rice", quantity: 9001 },
    { name: "Royal Jelly", quantity: 20 },
];

const newInv2 = [];
const currInv2 = [{ name: "Peanut Butter", quantity: 20 }];
const expected2 = [{ name: "Peanut Butter", quantity: 20 }];

const newInv3 = [{ name: "Peanut Butter", quantity: 20 }];
const currInv3 = [];
const expected3 = [{ name: "Peanut Butter", quantity: 20 }];

/**
 * Updates the current inventory based on the new inventory.
 * - Time: O(?).
 * - Space: O(?).
 * @typedef {Object} Inventory
 * @property {string} Inventory.name The name of the item.
 * @property {number} Inventory.quantity The quantity of the item.
 * @param {Array<Inventory>} newInv A shipment of new inventory.
 *    An array of inventory objects.
 * @param {Array<Inventory>} currInv
 * @return The currInv after being updated.
 function updateInventory(newInv, currInv) {
     var my_len = 0;
     if (newInv.length > currInv.length) {
         my_len = newInv.length;
        }
        if (newInv.length < currInv.length) {
            my_len = currInv.length;
        }
        for (var i = 0; i < my_len; i++) {
            for (var x = 0; x < my_len; x++) {
                console.log(newInv[i]['name'], currInv[x]['name'])
                
                if (newInv[i]['name'] == currInv[x]['name']) {
                    // console.log(currInv[x], newInv[i])
                    currInv[i]['quantity'] += newInv[x]['quantity']
                }
                
                else if (newInv[i]['name'] != currInv[x]['name'] && ){
                    currInv.push(newInv[x])
                }
            }
        }
        return currInv
        
    }
    */
function updateInventory(newInv, currInv) {
    var my_len = 0;
    if (newInv.length > currInv.length) {
        my_len = newInv.length;
    }
    if (newInv.length < currInv.length) {
        my_len = currInv.length;
    }
    for (var i = 0; i < my_len; i++) {
        for (var x = 0; x < my_len; x++) {
            console.log(newInv[i]['name'], currInv[x]['name'])
            if (newInv[i]['name'] != currInv[x]['name']) {
                continue
            }
            if (newInv[i]['name'] == currInv[x]['name']) {
                // console.log(currInv[x], newInv[i])
                currInv[i]['quantity'] += newInv[x]['quantity']
            }
            if (x == my_len) {
                console.log("append!")
            }
            else {
                currInv.push(newInv[x])
            }
        }
    }
    return currInv

}

console.log(updateInventory(newInv1, currInv1));

console.log(updateInventory(newInv1, currInv1));
module.exports = { updateInventory };



  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



/*
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Is there a quick way to determine if they aren't an anagram before spending more time?
Given two strings
return whether or not they are anagrams
 
const strA1 = "yes";
const strB1 = "eys";
const expected1 = true;
 
const strA2 = "yes";
const strB2 = "eYs";
const expected2 = true;
 
const strA3 = "no";
const strB3 = "noo";
const expected3 = false;
 
const strA4 = "silent";
const strB4 = "listen";
const expected4 = true;
 
/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.

function isAnagram(s1, s2) {}
 
module.exports = { isAnagram };
*/