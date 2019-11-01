// 1. input 태그 안의 값(value)를 잡는다.

// 2. button 에 'click' 이 일어났을 때 input 에 Enter 키를 쳤을 때 1에서 잡은 값을 요청으로 보낸다.
// [무엇].addEventListner([언제], [어떻게 type : function]])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const resultArea = document.querySelector('#js-result-area')

const func = function () {};

// const whenClicked = function () {
//     console.log('클릭 되었다.')
// }

// const whenPressed = function (event) {
//     console.log('꾸욱');
//     console.log(event);
// }

// 그 때 이 일을 해
button.addEventListener('click', () => {
    const inputValue = inputArea.value;
    // console.log(inputValue);
    // resultArea.innerHTML += inputValue;
    searchAndPush(inputValue);
});

inputArea.addEventListener('keypress', (event) => {
    
    if (event.which === 13) {
        const inputValue = inputArea.value;
        // console.log(inputValue);
        // inputValue로 Giphy API에 요청보내서 받기
        searchAndPush(inputValue);
    }
});

// 3. Giphy API 에서 넘겨준 Data를 index.html에서 보여준다.
// const pushToDOM = (data) => {
//     // 요청 => 응답을 받아서


//     // 화면에 보내준다.
//     resultArea.innerHTML += data;
// };


// const sendAjaxReq = () => {
//     const AJAX = XMLHttpRequest(); // 요청 준비
//     AJAX.open('GET', url);         // 요청 세팅
//     AJAX.send();                   // 요청 보내기

//     AJAX.addEventListener('load', (answer) => {
//         const res = answer.target.response;
//         const giphyData = JSON.parse(res);
//         console.log(giphyData);
//     })
// }
// 3. Giphy API 에서 넘겨준 Data를 index.html에서 보여준다.
const searchAndPush = (keyword) => {
    const API_KEY = 'b1b16HVxvzpPpV3W8RgcGmDAGKET09A5'
    const imageCount = document.querySelector('#js-image-count').value;
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=${imageCount}&offset=0&rating=G&lang=ko`
    const AJAX = new XMLHttpRequest(); // 요청 준비
    AJAX.open('GET', url);         // 요청 세팅
    AJAX.send();                   // 요청 보내기

    AJAX.addEventListener('load', (answer) => {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        const dataSet = giphyData.data;
        
        inputArea.value = null;
        resultArea.innerHTML = null;
        for (const data of dataSet) {
            pushToDOM(data.images.fixed_height.url);
        }
    });

    const pushToDOM = (imageUrl) => {
        const imageTag = document.createElement('img');
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-image';
        imageTag.classList.add('container-image');
        
        resultArea.appendChild(imageTag);
    }
};