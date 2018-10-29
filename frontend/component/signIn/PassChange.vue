<template>
    <div id="passChange">
        <input type="text" v-model="id" />
        <input type="text" v-model="email" />
        
        <router-link to = "/login">비밀번호 찾기</router-link>
        <router-link to = "/login">취소</router-link>
    </div>
</template>

<script>
export default {
    name: 'passChange',
    props: {
        id            : String,
        email         : String,
    }
}
</script>
