<template>
    <div id="main">
        {{ content }}
        <button @click="logout">로그아웃</button>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'main',
    data() {
        return {
            content: 'test',
        }
    },
    methods: {
        logout() {
            this.$store.dispatch('logout')    
        }
    },
    created() {
        this.$store.dispatch('setTokenFromServer')
    },
}
</script>
