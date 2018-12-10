<template>
    <div id="contentList">
        <ul>
            <content-view
                v-for="post in posts.slice(0, 20)" 
                :key="post.id"
                :id="post.id"
                :contents="post.contents"
                :username="post.username"
                :createdDate="post.createdDate"
                :convertDate="post.convert_date"
                :image="post.image"
                :mentionIndex="post.mentionIndex"
                :mentionDepth="post.mentionDepth"
                :mentionCount="post.mentionCount"
                :imageOpen="false"
            ></content-view>
        </ul>
    </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import ContentView from './ContentView.vue'

export default {
    name: 'contentList',
    components: {
        ContentView
    },
    computed: {
        ...mapState({
            posts: state => state.posts.posts
        })
    },
    methods: {
        ...mapActions(
            'posts', {
                getPosts: 'getPosts',
            }
        ),
    },
}
</script>
