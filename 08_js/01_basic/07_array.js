const numbers = [1, 2, 3, 4];

numbers[0];  // 1
numbers[-1]; // undefined : index는 양의 정수만 사용
numbers.length; // 4

// 원본 파괴 methods
numbers.reverse(); // return 도 있다.
numbers.reverse();
numbers.push('a'); // length가 return 됨
numbers.pop();
numbers.unshift('a');
numbers.shift();

// 원본 그대로인 methods
numbers.includes(1)  //1이 있나요?
numbers.indexOf(1) // 1의 index 어디에요?
numbers.join()  // "1,2,3" string으로 바꿈
numbers.join('')  // "123" string으로 바꿈

// method로 조작은 허용