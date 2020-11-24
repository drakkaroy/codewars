function cakes(recipe, available) {
    const calcList = [];
    for( const [key] of Object.entries(recipe)) {
        if (available[key] === undefined) return 0;
        if (Math.floor(available[key] / recipe[key]) > 0) {
            calcList.push(Math.floor(available[key] / recipe[key]))
        } else {
            return 0;
        }
    }
    return Math.min(...calcList);
}

// const test1 = cakes({"flour": 500, "sugar": 200, "eggs": 1}, 
// {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
// console.log(test1);
    
// const test2 = cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, 
// {"sugar": 500, "flour": 2000, "milk": 2000})
// console.log(test2);
