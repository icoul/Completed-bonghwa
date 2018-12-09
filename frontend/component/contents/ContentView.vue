<template>
    <li class="post">
        <div class="username"><span @click="callSendUsername">{{ username }}</span></div>
        <div class="contents" @click="mentions.length > 0 ? checkMentions() : callGetMentions()">
            <span>{{ contents }}</span>
            <span 
                v-if="image"
                @click="viewImage">[이미지]</span>
            <span
                v-if="mentionCount"
            > >>> </span>
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
        <mention-list
                v-if="mentionOpen"
                v-for="mention in mentions" 
                :key="mention.id"
                :id="mention.id"
                :contents="mention.contents"
                :username="mention.username"
                :createdDate="mention.createdDate"
                :convertDate="mention.convert_date"
                :image="mention.image"
                :mentionIndex="mention.mentionIndex"
                :mentionDepth="mention.mentionDepth"
                :imageOpen="false"
            ></mention-list>
    </li>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import EventBus from '../../service/EventBus'
import MentionList from './MentionList.vue'

export default {
    name: 'contentView',
    props: [
        "id", "contents", "username", "createdDate", "convertDate", 
        "image", "imageOpen", "mentionIndex", "mentionDepth", "mentionCount"
    ],
    components: {
        MentionList
    },
    data() {
        return {
            mentions: [],
            mentionOpen: false
        }
    },
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
        ...mapActions(
            'posts', {
                getMentions: 'getMentions',
            }
        ),
        checkMentions() {
            this.mentionOpen = (this.mentionOpen == false);
        },
        callGetMentions() {
            this.getMentions(this.id).then(result => {
                if (result) {
                    this.mentions = result;
                    this.mentionOpen = true;
                }
            });
        },
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
                    index: this.mentionIndex
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
