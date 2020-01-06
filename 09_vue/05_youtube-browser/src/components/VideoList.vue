<template>
    <ul class="list-group col-lg-4">
        <VideoListItem 
            v-for="video in videos" 
            :key="video.etag"
            :video="video"
            @videoSelect="onVideoSelect"
        >
        </VideoListItem>
    </ul>
</template>

<script>
import VideoListItem from './VideoListItem';
export default {
    name:'VideoList',
    // props 쓰기: step 1. props가 넘어온다고 명시한다. 여러 개 넘어올 수 있음! => []
    // props는 data랑 똑같이 쓸 수 있음. props == 물려받은 data! 그냥 바로 쓰면 됨!
    // props: ['videos'],  배열로 써도 되지만 객체를 매우 권장
    props: {
        videos: Array, // Validation. videos가 array냐
    },
    /* 절대 이렇게 하면 안됨
    data () {
        return {
            videos: this.videos
        }
    }*/
    components: {
        VideoListItem,
    },
    methods: {
        onVideoSelect (video) {
            this.$emit('videoSelect', video)
        }
    }
}
</script>

<style>
    
</style>