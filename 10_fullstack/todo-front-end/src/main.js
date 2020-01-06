import Vue from 'vue'
import App from './App.vue'
import router from './router'
// from '.router/index.js'가 생략됨.
// 이름이 반드시 index.js여야 함.

import store from './store'
// from '.store/index.js'가 생략됨.
// 이름이 반드시 index.js여야 함.

import VueSession from 'vue-session'
// 발급받은 Token을 SessionStorage에 저장하는 걸 도와줌.


Vue.config.productionTip = false;
Vue.use(VueSession);   // Vue에게 Vuesession이라는 Middleware 등록

new Vue({
  router,  // router/index.js에서 악수하고, 본격적으로 일 시작. (실무 영역)
  // router : router와 같은 말
  store,  // store/index.js에서 악수하고, 본격적으로 일 시작. (실무 영역)
  // store : store와 같은 말
  render: h => h(App)
}).$mount('#app')