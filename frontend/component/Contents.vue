<template>
    <div id="contents">
        {{ content }}
        <div @click="getUsers()">test</div>
        <router-link to="/test">go Test</router-link>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'contents',
    data() {
        return {
            content: 'test'
        }
    },
    methods: {
        ...mapActions({
            getUsers: 'getUsers'
        }),
    }
}
</script>
