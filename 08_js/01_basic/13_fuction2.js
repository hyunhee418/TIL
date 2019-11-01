// 1. 선언형
function a (x, y) {
    return x + y;
}

// 2. 할당형
const b = function (x, y) {
    return x + y;
};

// 3. Arrow function (할당형)

const c = (x, y) => {
    return x + y;
};

// 3-1. 짧게: 함수 블록에 코드가 return 문 한 줄이라면 {} + return 생략
const d = (x, y) => x + y;

// 3-2. 짧게 : 함수 인자가 단 하나! 일 때 () 생략
const e = x => {
    return x ** 2;
};

// 3-3. 인자가 1개이고, return 포함 한 줄 일 때
const square = x => x ** 2

// 3-4. 인자가 하나도 없으면
const f = () => {  // 없으면 ()  써야함
    return false;
};

const g = _ => {  // 없으면 _ 로 쓰기도 함
    return false;
};

