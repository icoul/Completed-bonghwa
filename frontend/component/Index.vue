<template>
    <div id="index">
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'index',
    methods: {
        ...mapActions('account', {
            setUserFromServer: 'setUserFromServer'
        })
    },
    created() {
        this.setUserFromServer();
    },
}
</script>
