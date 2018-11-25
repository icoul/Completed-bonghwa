<template>
    <div id="index">
    </div>
</template>

<script>
import { mapActions } from 'vuex'
import router from 'vue-router'

export default {
    name: 'index',
    methods: {
        ...mapActions('account', {
            setUserFromServer: 'setUserFromServer'
        })
    },
    created() {
        this.setUserFromServer().then(valid => {
            if (valid) {
                this.$router.push('main');
            } else {
                this.$router.push('login');
            }
        });
    },
}
</script>
