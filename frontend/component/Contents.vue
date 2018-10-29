<template>
    <div id="contents">
        {{ content }}
        <div @click="getToken">test</div>
        <router-link to="/login">go Test</router-link>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'contents',
    data() {
        return {
            content: 'test',
            token: ''
        }
    },
    computed: {
        ...mapActions([
            'getToken'
        ]),
    },
    methods: {
        
    }
}
</script>
