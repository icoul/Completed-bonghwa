<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
import Contents from './component/Contents.vue'
import SignIn from './component/SignIn.vue'
import { mapGetters } from 'vuex';

export default {
    name: 'app',
    data() {
        return {
            
        }
    },
    components: {
        Contents,
        SignIn
    },
    computed: mapGetters({
        token: 'checkToken'
    }),
}
</script>

<style>
</style>
