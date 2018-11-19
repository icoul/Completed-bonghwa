<template>
    <div id="passChange">
        <form @submit.prevent="callFindPass">
            <input type="text" v-model="info.id" />
            <input type="text" v-model="info.email" />
            
            <button>비밀번호 찾기</button>
            <router-link to = "/login">취소</router-link>
        </form>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
    name: 'passChange',
    data() {
        return {
            info: {
                id: '1',
                email: 'icoul@naver.com',
            }
        }
    },
    computed: {
        ...mapState('account', ['state'])
    },
    methods: {
        ...mapActions('account', ['findPass']),
        callFindPass() {
            this.findPass(this.info)
        }
    }
}
</script>
