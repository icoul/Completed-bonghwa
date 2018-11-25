<template>
    <div id="main">
        <div>
            <input type="text" name="content" v-model="post.content" v-bind:placeholder="error" />
            <button @click="callSendPost" v-bind:disabled="post.content == ''">전송</button>
        </div>
        <ul>
            <li v-for="post in posts" :key="post.no">
                {{ post.contents }} {{ post.username }} {{ post.created_date }}
            </li>
        </ul>
        <button @click="callLogout">로그아웃</button>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex'

export default {
    name: 'main',
    data() {
        return {
            post: {
                content: '',
                writer: ''
            },
            error: ''
        }
    },
    computed: {
        ...mapState({
            account: state => state.account.user,
            users: state => state.users,
            posts: state => state.posts.posts
        })
    },
    methods: {
        ...mapActions(
            'account', {
                callLogout: 'logout',
                setUserFromServer: 'setUserFromServer'
            }
        ),
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
    created() {
        this.setUserFromServer().then(valid => {
            if(valid) {
                this.getPosts();
                this.post.writer = this.account.username;
            }
        });
    },
}
</script>
