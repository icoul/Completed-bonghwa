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
            <span>{{ post.image.name }}</span>
            <input 
                type="file" 
                name="image" 
                @change="viewFileName($event.target.files)" 
            />
    </div>
</template>

<script>
import { mapActions } from 'vuex'
import EventBus from '../../service/EventBus'

export default {
    name: 'writeForm',
    data() {
        return {
            post: {
                content: '',
                mentionIndex: 0,
                mentionDepth: 0,
                mentionId: 0,
                image: new Object()
            },
            error: '',
        }
    },
    created() {
        EventBus.$on('sendUsername', this.sendUsername);
        EventBus.$on('sendSecret', this.sendSecret);
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
                mentionIndex: 0,
                mentionDepth: 0,
                image: new Object()
            };
        },
        callSendPost() {
            // 멘션을 보내는 상태인지 체크. @id 가 없으면 index, depth 초기화
            if(!this.mentionCheck()) {
                this.post.mentionIndex = 0;
                this.post.mentionDepth = 0;
                this.post.mentionId = 0;
            }

            // FormData에 데이터 삽입
            const form = new FormData();
            Object.keys(this.post).forEach(key => form.append(key, this.post[key]));
            this.sendPost(form).then(({result, message}) => {
                if(result == '0') {
                    alert(message);
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
            
            this.post.image = files[0];
        },
        sendUsername(map) {
            let target = map.contents.replace(`@${map.username}`, '').match(/(@\S+)/g);

            if (target == null) {
                target = '';
            } else {
                target = target.join(' ')
            }

            this.post.content = `@${map.username} ${target} ${this.post.content}`;
            this.post.mentionIndex = map.index;
            this.post.mentionDepth = map.depth;
            this.post.mentionId = map.id;

            window.scrollTo(0, 0);
        },
        sendSecret(map) {
            this.post.content = `!${map.username} ${this.post.content}`;
            this.post.mentionIndex = map.index;
            this.post.mentionDepth = map.depth;
            this.post.mentionId = map.id;

            window.scrollTo(0, 0);
        },
        mentionCheck() {
            const mention = /(@[\w]+ )/;
            const secret = /(^!\S+ )/;
            return mention.exec(this.post.content) || secret.exec(this.post.content)
        }
    },
}
</script>

<style>
    input[name=image] { width: 60px; position: absolute; left: 222px; opacity: 0;}
</style>
