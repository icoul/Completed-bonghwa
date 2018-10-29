<template>
    <div id="login">
        <input type="text" id="loginId" name="id" />
        <input type="password" id="loginPass" name="password" />
        <router-link to = "/loginCheck">로그인</router-link>
        <router-link to = "/signUp">회원가입</router-link>
        <router-link to = "/passChange">비밀번호 찾기</router-link>
    </div>
</template>

<script>
export default {
    name: 'signIn',
    data() {
        return {
            
        }
    },
}
</script>