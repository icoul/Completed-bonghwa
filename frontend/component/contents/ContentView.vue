<template>
    <li class="post">
        <div class="username"><span @click="isSecret ? sendSecret() : sendUsername()">{{ username }}</span></div>
        <div class="contents" @click="mentions.length > 0 ? checkMentions() : callGetMentions()">
            <div 
                :class="{ 'secret' : isSecret }"
                v-html="boldContents"></div>
            <div 
                v-if="image"
                @click="viewImage">[이미지]</div>
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
        boldContents() {
            const target = this.contents.match(/(@\S+)/g);
            let boldContents = this.contents;

            if (target == null) {
                return boldContents;
            }

            target.forEach(username => {
                boldContents = boldContents.replace(username, `<span class="mention">${username}</span>`);
            });

            return boldContents
        },
        isSecret() {
            if (this.contents[0] != '!') {
                return false
            }

            return true
        },
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
            const form = new FormData();
            form.append("postId", this.id);
            form.append("mentionIndex", this.mentionIndex);
            form.append("mentionDepth", this.mentionDepth);

            this.getMentions(form).then(result => {
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
        sendUsername() {
            EventBus.$emit("sendUsername", 
                { 
                    username: this.username,
                    contents: this.contents,
                    id: this.id,
                    index: this.mentionIndex,
                    depth: this.mentionDepth
                }
            )
        },
        sendSecret() {
            EventBus.$emit("sendSecret", 
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
    .post .contents div {float: left;}
    .post .contents div.secret {color: grey;}
    .post .contents div span {font-weight: bold;}
</style>
