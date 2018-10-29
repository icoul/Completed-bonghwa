<template>
    <div id="signUp">
        <ul>
            <li>id : <input type="text" v-model="id" /></li>
            <li>password : <input type="password" v-model="password" /></li>
            <li>password check : <input type="password" v-model="checkPassword" /></li>
            <li>email : <input type="text" v-model="email" /></li>
        </ul>
        <router-link to = "/login">회원가입</router-link>
        <router-link to = "/login">취소</router-link>
    </div>
</template>

<script>
export default {
    name: 'signUp',
    props: {
        id            : String,
        password      : String,
        checkPassword : String,
        email         : String,
    }
}
</script>

