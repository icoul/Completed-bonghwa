<template>
    <div id="login">
        <input type="text" v-model="id" />
        <input type="password" v-model="password" />
        <a @click="loginCheck">로그인</a>
        <router-link to = "/signUp">회원가입</router-link>
        <router-link to = "/passChange">비밀번호 찾기</router-link>
    </div>
</template>

<script>
export default {
    name: 'signIn',
    data() {
        return {
            id: 'a',
            password: 'b'    
        }
    },
    methods: {
        loginCheck() {
            var map = {'id': this.id, 'password': this.password}
            this.$store.dispatch('loginCheck', map)
        }
    }
}
</script>