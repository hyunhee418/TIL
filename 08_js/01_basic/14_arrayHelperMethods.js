// 14_arrayHelperMethods.js
// ES5
var colors = ['red', 'blue', 'green']

for (var i=0; i < colors.length; i++) {
    console.log(colors[i]);
}

// ES6+ forEach 끝나고 아무것도  return 하지 않는다.
colors.forEach(function (x) {
    console.log(x)
})

// ES5
const numbers = [1, 2, 3];
const doubledNumbers = [];

for (let i=0; i < numbers.length; i++) {
    doubledNumbers.push(numbers[i] * 2);
}
console.log(doubledNumbers)

// ES6
/*
    map(lambda number: number * 2, numbers)
*/
numbers.map(function(number) {
    return number * 2;
})

const tripleNumbers = numbers.map(function(number) {
    return number * 3;
})

console.log(tripleNumbers)

// ES5
const products = [
    {name: 'apple', type:'fruit'},
    {name: 'carrot', type:'vegetable'},
    {name: 'tomato', type:'fruit'},
    {name: 'cucumber', type:'vegetable'},
]

const fruits = [];

for (const product of products) {
    if (product.type === 'fruit') {
        fruits.push(product);
    };
};
console.log(fruits);

// ES6+
const vegetables = products.filter((product) => {
    return product.type === 'vegetable';
});
console.log(vegetables);