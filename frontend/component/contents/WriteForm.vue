<template>
    <div id="writeForm">
            <input 
                type="text" 
                name="content" 
                v-model="post.content"
                v-on:keyup.enter="callSendPost"
                v-bind:placeholder="error"
             />
            <button 
                @click="callSendPost" 
                v-bind:disabled="post.content.length == 0"
            >전송</button>
            <a href="*" >[이미지]</a>
            <span>{{ post.imageName }}</span>
            <input 
                type="file" 
                name="image" 
                @change="viewFileName($event.target.files)" 
            />
    </div>
</template>

<script>
import { mapActions } from 'vuex'
import ContentList from './ContentList.vue'

export default {
    name: 'writeForm',
    data() {
        return {
            post: {
                content: '',
                writer: '',
                imageName: ''
            },
            imageForm: new FormData(),
            error: '',
        }
    },
    methods: {
        ...mapActions(
            'posts', {
                getPosts: 'getPosts',
                sendPost: 'sendPost',
                uploadImage: 'uploadImage'
            }
        ),
        initWriteForm() {
            this.post = {
                content: '',
                writer: '',
                imageName: ''
            };
            this.imageForm = new FormData();
        },
        callSendPost() {
            this.imageForm.append('contents', this.post.content);
            this.sendPost(this.imageForm).then(({result, message}) => {
                if(result == '0') {
                    alert(message)
                } else {
                    this.getPosts();
                    this.initWriteForm();
                }
            });
        },
        viewFileName(files) {
            if (!files.length) {
                return;
            }

            this.post.imageName = files[0].name;
            this.imageForm.append('file', files[0], files[0].name);
        },
    },
}
</script>

<style>
    input[name=image] { width: 60px; position: absolute; left: 222px; opacity: 0;}
</style>
