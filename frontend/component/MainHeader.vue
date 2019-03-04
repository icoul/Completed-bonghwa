<template>
    <div id="header">
        <div class="leftHeader">
            <ul class="sortBtn">
                <li :class="{ 'on' : sortOption == 'all' }" 
                    @click="sortContents('all')">전체보기</li>
                <li :class="{ 'on' : sortOption == 'mention' }" 
                    @click="sortContents('mention')">멘션만 보기</li>
                <li :class="{ 'on' : sortOption == 'my' }" 
                    @click="sortContents('my')">내 포스트 보기</li>
                <li :class="{ 'on' : sortOption == 'secret' }" 
                    @click="sortContents('secret')">비밀 멘션 보기</li>
            </ul>
        </div>
        <div class="rightHeader">

        </div>
    </div>
</template>

<script>
import EventBus from '../service/EventBus'

export default {
    name: 'mainHeader',
    data() {
        return {
            sortOption : 'all'
        }
    },
    methods: {
        sortContents(option) {
            this.sortOption = option;
            EventBus.$emit('sortPosts', option);

            socket.send(JSON.stringify({
                'message': 'aaa'
            }));
        }
    }
}
</script>

<style>
    .leftHeader .sortBtn .on {background: blue;}
</style>
