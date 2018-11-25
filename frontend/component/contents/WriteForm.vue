<template>
    <div id="writeForm">
        <input type="text" name="content" v-model="post.content" v-bind:placeholder="error" />
        <button @click="callSendPost" v-bind:disabled="post.content == ''">전송</button>
        <a href="*">[이미지]</a><span>{{ imageName }}</span>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex'
import ContentList from './ContentList.vue'

export default {
    name: 'writeForm',
    data() {
        return {
            post: {
                content: '',
                writer: ''
            },
            error: '',
            imageName: ''
        }
    },
    methods: {
        ...mapActions(
            'posts', {
                getPosts: 'getPosts',
                sendPost: 'sendPost'
            }
        ),
        callSendPost() {
            this.sendPost(this.post).then(({result, message}) => {
                if(result == '0') {
                    alert(message)
                } else {
                    this.getPosts();
                    this.post.content = '';
                }
            });
        }
    },
}
</script>
