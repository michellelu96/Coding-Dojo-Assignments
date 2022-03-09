
/* 
    https://visualgo.net/en/sorting
    Selection sort works by iterating through the list, finding the minimum
    value, and moving it to the beginning of the list. Then, ignoring the first
    position, which is now sorted, iterate through the list again to find the
    next minimum value and move it to index 1. This continues until all values
    are sorted.
    Unstable sort.
    Time Complexity
        - Best: O(n^2) quadratic.
        - Average: O(n^2) quadratic.
        - Worst: O(n^2) quadratic.
    
    Space: O(1) constant.
    Selection sort is one of the slower sorts.
        - ideal for: pagination, where page 1 displays 10 records for example,
        you run selection sort for 10 iterations only to display the first 10
        sorted items...
*/
const myArr = [3, 2, 9, 5, 1, 4, 8]

function selectionSort(arr) {
    for(let i = 0;i < arr.length -1;i++){
        let min = i;
        for (let x = i; x < arr.length;x++){
            if(arr[x] < arr[min]){
                min = x;
            }
        }
        [arr[i],arr[min]] = [arr[min],arr[i]];
    }
    return arr
}

console.log(selectionSort(myArr))