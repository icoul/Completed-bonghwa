<template>
    <div id="signUp">
        <ul>
            <li>id : <input type="text" name="id" v-model="id" v-validate="'required'" /><p v-if="$errors.has('id')" v-text="$errors.first('id')"></p></li>
            <li>password : <input type="password" name="password" v-model="password" v-validate="'required|minLen6'" /><p v-if="$errors.has('password')" v-text="$errors.first('password')"></p></li>
            <li>password check : <input type="password" name="checkPassword" v-model="checkPassword" v-validate="'required|equalPass'" /><p v-if="$errors.has('checkPassword')" v-text="$errors.first('checkPassword')"></p></li>
            <li>email : <input type="text" name="email" v-model="email" v-validate="'required'" /><p v-if="$errors.has('email')" v-text="$errors.first('email')"></p></li>
        </ul>
        <button @click="signUp">회원가입</button>
        <router-link to = "/login">취소</router-link>
    </div>
</template>

<script>
export default {
    name: 'signUp',
    data() {
        return {
            user : {
                id: '',
                password: '',
                checkPassword: '',
                email: '',
            },
        }
    },  
    methods: {
        signUp() {
            this.$validator.validateAll()
        },
    }
}
</script>

