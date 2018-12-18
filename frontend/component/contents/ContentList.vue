<template>
    <div id="contentList">
        <ul>
            <content-view
                v-for="post in posts" 
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
import EventBus from '../../service/EventBus'
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
                addPosts: 'addPosts',
                sortPosts: 'sortPosts'
            }
        ),
        scrollHandler(event) {
            window.removeEventListener('scroll', this.scrollHandler);
            var s = window.pageYOffset
            var h = window.innerHeight
            var b = document.documentElement.scrollHeight
            
            if (Math.floor(s) + h > b - 2){
                this.addPosts().then(valid => {
                    if (valid) {
                        window.addEventListener('scroll', this.scrollHandler);        
                    }
                });
            } else {
                window.addEventListener('scroll', this.scrollHandler);
            }
        },
    },
    created() {
        // 스크롤 이벤트 등록
        window.addEventListener('scroll', this.scrollHandler);
        // 이벤트 버스 등록
        EventBus.$on('sortPosts', this.sortPosts);
    },
    destroyed() {
        // 스크롤 이벤트 제거
        window.removeEventListener('scroll', this.scrollHandler);
    }
}
</script>
