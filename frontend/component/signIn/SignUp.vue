<template>
    <div id="signUp">
        <form @submit.prevent="callSignUp">
            <ul>
                <li>username : <input type="text" name="username" v-model="user.username" v-validate="'required'" /><p v-if="$errors.has('username')" v-text="$errors.first('username')"></p></li>
                <li>password : <input type="password" name="password" v-model="user.password" v-validate="'required|minLen6'" /><p v-if="$errors.has('password')" v-text="$errors.first('password')"></p></li>
                <li>password check : <input type="password" name="checkPassword" v-model="user.checkPassword" v-validate="'required|equalPass'" /><p v-if="$errors.has('checkPassword')" v-text="$errors.first('checkPassword')"></p></li>
                <li>email : <input type="text" name="email" v-model="user.email" v-validate="'required'" /><p v-if="$errors.has('email')" v-text="$errors.first('email')"></p></li>
            </ul>
            <button>회원가입</button>
            <router-link to = "/login">취소</router-link>
        </form>
    </div>
</template>

<script>
import sha256 from 'sha256'
import { mapState, mapActions } from 'vuex'

export default {
    name: 'signUp',
    data() {
        return {
            user : {
                username: '1',
                password: '111111',
                checkPassword: '111111',
                email: '111111',
            },
        }
    }, 
    computed: {
        ...mapState('account', ['state'])
    },
    methods: {
        ...mapActions('account', ['signUp']),
        callSignUp() {
            this.$validator.validateAll().then(valid => {
                if (valid) {
                    this.user.password = sha256(this.user.password);
                    this.user.checkPassword = this.user.password;
                    this.signUp(this.user);
                    this.signUpFormInit();
                }
            });
        },
        signUpFormInit() {
            this.user.password = '';
            this.user.checkPassword = '';
        }
    }
}
</script>

