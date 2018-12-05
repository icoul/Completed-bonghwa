<template>
    <li class="post">
        <div class="username"><span @click="callSendUsername">{{ username }}</span></div>
        <div class="contents">
            {{ contents }}
            <span 
                v-if="image"
                @click="viewImage">[이미지]</span>
        </div>
        <div class="postDate">
            {{ convertDate }}
            <span 
                v-if="myPost"
                @click="deletePost">[x]</span>
        </div>
        <div v-if="hasImage && imageOpen">
            <img height="200" :src="imageUrl" />
        </div>
    </li>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import EventBus from '../../service/EventBus'

export default {
    name: 'contentView',
    props: [
        "id", "contents", "username", "createdDate", "convertDate", 
        "image", "imageOpen", "mentionIndex", "mentionDepth"
    ],
    computed: {
        myPost() {
            return this.$store.getters['account/getUsername'] === this.username
        },
        hasImage() {
            return this.image !== null
        },
        imageUrl() {
            return this.hasImage ? '../static/image/' + this.image : ''
        }
    },
    methods: {
        viewImage() {
            this.imageOpen = this.imageOpen == false
        },
        deletePost() {
            if (confirm("삭제하시겠습니까?")) {
                this.$store.dispatch('posts/deletePost', this.id).then(valid => {
                    if (valid) {
                        this.$store.dispatch('posts/getPosts');
                    } else {
                        alert('삭제에 실패했습니다.')
                    }
                });     
            }
        },
        callSendUsername() {
            EventBus.$emit("sendUsername", 
                { 
                    username: this.username,
                    id: this.id,
                    index: this.mentionIndex,
                    depth: this.mentionDepth
                }
            )
        }
    }
}
</script>

<style>
    ul, li {list-style: none;}
    .post .username {float: left; width: 100px;}
    .post .username span:hover {color: blue; text-decoration: underline; cursor: pointer;}
    .post .contents {float: left; width: 700px;}
</style>
