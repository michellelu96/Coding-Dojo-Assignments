// 1
var hello = 'world';
console.log(hello);
//world

//2
var needle = 'haystack';
function test() {
    var needle = 'magnet';
    console.log(needle);
}
test();
//magnet


//3
var brendan = 'super cool';
function print() {
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);
//supercool

//4
var food = 'chicken';
function eat() {
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}
console.log(food);
eat();
// chicken
//half-chicken

//5
var mean = function() {
    food = "chicken";
    console.log(food);
    var food = "fish";
    console.log(food);
}
console.log(food);
mean();
console.log(food);
// errors because food is not declated outside

//

//6
var genre = "disco";
function rewind() {
    var genre = "r&b";
    console.log(genre);
    genre = "rock";
    console.log(genre);
}
console.log(genre);
rewind();
console.log(genre);
//disco
//r&b
//rock
//disco


//7
dojo = "san jose";
function learn() {
    dojo = "seattle";
    console.log(dojo);
    var dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);
learn();
console.log(dojo);
//san jose
//seattle
//burbank
//san jose

//8
function makeDojo(name, students){
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if(dojo.students > 50){
        dojo.hiring = true;
    }
    else if(dojo.students <= 0){
        dojo = "closed for now"; // error because you can't change const.
    }
    return dojo;
}
console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
//name: chicago, students: 65, hiring:true
//error because you can't change const.








