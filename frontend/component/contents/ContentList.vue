<template>
    <div id="contentList">
        <ul>
            <li v-for="post in posts" :key="post.no">
                {{ post.contents }} {{ post.username }} {{ post.created_date }}
            </li>
        </ul>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex'

export default {
    name: 'contentList',
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
