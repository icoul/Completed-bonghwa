<template>
    <div id="main">
        <write-form ref="writer"></write-form>
        <content-list ref="content"></content-list>
        <button @click="callLogout">로그아웃</button>
    </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import WriteForm from './contents/WriteForm.vue'
import ContentList from './contents/ContentList.vue'

export default {
    name: 'main',
    components: {
        WriteForm,
        ContentList
    },
    computed: {
        ...mapState({
            account: state => state.account.user,
            users: state => state.users,
        })
    },
    methods: {
        ...mapActions(
            'account', {
                callLogout: 'logout',
                setUserFromServer: 'setUserFromServer'
            }
        ),
    },
    created() {
        // 로그인 여부 체크
        this.setUserFromServer().then(valid => {
            if(valid) {
                this.$refs.content.getPosts();
            } else {
                this.$router.push('login');
            }
        });
    }
}
</script>
