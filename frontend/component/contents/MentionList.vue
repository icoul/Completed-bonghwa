<template>
    <li class="mention">
        <div class="username"><span>{{ username }}</span></div>
        <div class="contents">
            <span>{{ contents }}</span>
            <span 
                v-if="image"
                @click="viewImage">[이미지]</span>
        </div>
        <div class="postDate">
            {{ convertDate }}
        </div>
        <div v-if="hasImage && imageOpen">
            <img height="200" :src="imageUrl" />
        </div>
    </li>
</template>

<script>
import EventBus from '../../service/EventBus'

export default {
    name: 'mentionList',
    props: [
        "id", "contents", "username", "createdDate", "convertDate", 
        "image", "imageOpen", "mentionIndex", "mentionDepth"
    ],
    computed: {
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
    }
}
</script>

<style>
    .post .mention {padding-left: 50px; background: #ddd;}
    .post .mention .contents {width: 650px;}
</style>
