<template>
    <li class="mention">
        <div>{{ contents }}</div>
    </li>
</template>

<script>
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
    }
}
</script>
