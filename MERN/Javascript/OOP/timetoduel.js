class Card {
    constructor(name,cost){
        this.name = name;
        this.cost = cost;
    }
}

class Unit extends Card {
    constructor(name,cost,power,res){
        super(name,cost)
        this.power = power;
        this.res=res;
    }
    attack( target ) {
        if( target instanceof Unit ) {
            target.res -= this.power
        } else {
            throw new Error( "Target must be a unit!" );
        }
    }
}

class Effect extends Card {
    constructor(name,cost,text,stat,magnitude){
        super(name,cost)
        this.text = text;
        this.stat = stat;
        this.magnitude=magnitude;
    }
    play( target ) {
        if( target instanceof Unit ) {
            this.stat =="power"
            ? target.power += this.magnitude
            : target.res += this.magnitude;
        } else {
            throw new Error( "Target must be a unit!" );
        }
    }
}

const redBeltNinja = new Unit("Red Belt Ninja",3,3,4);
console.log(redBeltNinja);
const hardAlgorithm = new Effect("Hard Algorithm",2,"Increase target's resilience by 3","resilience",3);
console.log(hardAlgorithm);
hardAlgorithm.play(redBeltNinja);

const blackBeltNinja = new Unit("Black Belt Ninja",4,5,4);
console.log(blackBeltNinja);
const unhandled = new Effect("Unhandled Promise Rejection",1,"Reduce target's resilience by 2","resilience",-2);
console.log(unhandled);
unhandled.play(redBeltNinja);
console.log(redBeltNinja)
const pairProgramming = new Effect("Pair Programming",3,"Increase target's power by 2","power",2)
pairProgramming.play(redBeltNinja);
console.log(redBeltNinja);

redBeltNinja.attack(blackBeltNinja)
console.log(blackBeltNinja)
