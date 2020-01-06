<template>
    <div>
        <li @click="onVideoClick" class="list-group-item">
            <img :src="thumbnailUrl" class="mr-3" :alt="video.snippet.title">
            <div class="media-body">
                <span v-html="video.snippet.title"> </span>
            </div>
        </li>
    </div>
</template>
<script>
export default {
    name: 'VideoListItem',
    props: {
        video: Object,
    },
    computed: {
        thumbnailUrl () {  // data를 가공해서 값을 내뱉을 때
            return this.video.snippet.thumbnails.default.url
        }
    },
    methods:{
        onVideoClick () {
            this.$emit('videoSelect', this.video)
        }
    }
}
</script>

<style scoped>
    li {
        display: flex;
        cursor: pointer;
    }
    li:hover {
        background-color: #eee;
    }
</style>