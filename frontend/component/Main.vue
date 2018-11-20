<template>
    <div id="main">
        <div>
            <input type="text" v-model="post.content" />
            <button @click="sendPost(post)">전송</button>
        </div>
        <ul>
            <li v-for="post in posts" :key="post.no">
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
            }
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
                getPosts: 'getPosts'
            }
        )
    },
    created() {
        this.setUserFromServer();
        this.getPosts();
        console.log(this.posts)
    },
}
</script>
