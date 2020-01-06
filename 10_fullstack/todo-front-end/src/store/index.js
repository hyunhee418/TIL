import Vuex from 'vuex';
import Vue from 'vue';
import auth from './modules/auth'
Vue.use(Vuex); // Vue에 Vuex 미들웨어 등록

const store = new Vuex.Store({
    modules: {
        auth
    }
})

// 모듈이 모여서 store 가 된다.

export default store;