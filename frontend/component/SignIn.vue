<template>
    <div id="signIn">
        <login></login>
        <sign-up></sign-up>
        <pass-change></pass-change>
    </div>
</template>

<script>
import login from './signIn/Login.vue'
import signUp from './signIn/SignUp.vue'
import passChange from './signIn/PassChange.vue'

export default {
    name: 'signIn',
    data() {
        return {
            
        }
    },
    components: {
        login,
        signUp,
        passChange
    },
    methods: {
        signUp() {

        },
        passChange() {

        }
    }
}
</script>
