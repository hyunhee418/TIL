// JS : Non-Blocking
function sleep_3s() {
    setTimeout(() => {console.log('Wake Up!');}, 3000);
}


console.log('Start sleeping');
sleep_3s()
console.log('End of program')

// Non blocking 한 함수/ 작업들은?
/*
    지금 당장 해결할 수 없고
    결과도 확신할 수 없는 모든 일
*/

function complexTase () {
    console.log('start');
    for(let i=0; i<1000011000010; i++){};
    console.log('오래걸림');
    
}

setTimeout(() => {console.log('짱빨리 끝남!')}, 1)
complexTase()

// setTimeout은 언제 끝날 지 모르니까 나중에 할래
// 따라서 javascript갖고 일하는 거 하지마 왔다갔다 하는 거 정리하게 해줘