// auth.js 인증관련 모든 State를 작성.
// State에 접근/ 변경하는 모든 로직은 여기로.

const state = {
    token: null,
};

// Vuex 에서는 Arrow Function을 씀
const getters = {
    isLoggedIn: state => !!state.token,   // 특정 값을 true/false로 바꾸는 구문
};

const mutations = {
    setToken: (state, token) => state.token = token,
};

const actions = {
    // logout: (options) => {
    //     // mutations.setToken(state, null) 절대 안됨 === Very Bad
    //     options.commit('setToken', null)  // GREAT mutations는 commit을 이용하여 실행
    // },
    // 직접 꺼내지 않는 간편한 방법
    // 받아올 때 꺼내서 적용하기
    logout: ({ commit }) => {
        commit('setToken', null)
    },    

    login: ({ commit }, token) => {
        commit('setToken', token)
    }
};

export default {
    state, getters, mutations, actions,
}