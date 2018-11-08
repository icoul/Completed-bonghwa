<template>
    <div id="index">
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'index',
    data() {
        return {
      
        }
    },
    created() {
        this.$store.dispatch('setTokenFromServer')
    },
}
</script>
