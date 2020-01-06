<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> | 
        <span v-if="!isLoggedIn">
          <router-link to="/login">Login</router-link>
        </span>
        <span v-else>
          <a @click.prevent="logout" href="">Logout</a>
        </span>
    </div>
    <div class="container col-6">
      <router-view/>  <!-- login을 누르면 router의 /login이 되고 component에 LoginForm으로 가라고 되어있어서 거기로 가서 render되는 html은 routerview자리로 들어감 -->
    </div>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'App',
  methods: {
    ...mapGetters(['isLoggedIn']),
    ...mapActions(['logout']),
  }
}
</script>
<style>
/*
  1. 컴포넌트마다 비슷한/같은 함수들을 정의해야 함. + 정리가 안됨
  2. 사용자 auth 정보 & todos 목록을 컴포넌트끼리 공유하지 못함.

  Vuex(State Management System)
 */
</style>
