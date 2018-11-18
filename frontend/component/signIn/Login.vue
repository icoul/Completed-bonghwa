<template>
    <div id="login">
        <input type="text" v-model="id" />
        <input type="password" v-model="password" />
        <a @click="login">로그인</a>
        <router-link to = "/signUp">회원가입</router-link>
        <router-link to = "/passChange">비밀번호 찾기</router-link>
    </div>
</template>

<script>
import sha256 from 'sha256'
import { mapState, mapActions } from 'vuex';

export default {
    name: 'signIn',
    data() {
        return {
            id: 'a',
            password: 'b'    
        }
    },
    computed: {
        ...mapState('account', ['status'])
    },
    methods: {
        ...mapActions('account', ['loginCheck']),
        login() {
            var encryptionPass = sha256(this.password)
            var map = {'id': this.id, 'password': encryptionPass}
            this.loginCheck(map)
        }
    }
}
</script>