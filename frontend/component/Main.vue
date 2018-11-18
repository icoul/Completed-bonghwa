<template>
    <div id="main">
        {{ content }}
        <button @click="callLogout">로그아웃</button>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex'

export default {
    name: 'main',
    data() {
        return {
            content: 'test',
        }
    },
    computed: {
        ...mapState('account', ['state'])
    },
    methods: {
        ...mapActions('account', ['logout']),
        callLogout() {
            this.logout()
        }
    },
    created() {
        this.setTokenFromServer()
    },
}
</script>
