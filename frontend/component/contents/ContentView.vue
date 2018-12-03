<template>
    <li>
        {{ username }} 
        {{ contents }}
        <span 
            v-if="image"
            @click="viewImage">[이미지]</span> 
        {{ convertDate }}
        <span 
            v-if="myPost"
            @click="deletePost">[x]</span>
        <div v-if="hasImage && imageOpen">
            <img height="200" :src="imageUrl" />
        </div>
    </li>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'contentView',
    props: [
        "id", "contents", "username", "createdDate", "convertDate", "image", "imageOpen"
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
        }
    }
}
</script>
