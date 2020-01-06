// 17_primitiveDataType.js

typeof true;  // boolean
typeof false;

// 없다. 확실히 없다. 의도함
typeof null;  // object
// 아 몰라... 의도하지 않음
typeof undefined;  // undefined

typeof 'asdf';   //string
typeof 1;      // number
typeof 1.1;   // number
typeof Infinity;   // number
typeof NaN;   // number

typeof {} // object
typeof [] // object
typeof [1, 2];  // object
Array.isArray([1, 2]) // True
typeof {a:1, b:2};  // object

typeof function(){};  // function


// method와 function
// 객체에게 종속되어 실행있는 함수는 method
// 