import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)

// use는 계약서 도장( 우리 같이 일해보자. 악수 )

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
     path: '/login',
     name: 'login',
     component: Login
    },
  ],
})

export default router


// # sign 뒤에는 브라우저가 무시하고 그 뒤로는 vue가 다함.
// 따라서 일반적인 브라우저 라우팅 방식을 쓰기 위해 (# sign 을 없애기 위해) mode:'history' 사용 