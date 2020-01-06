<!-- single file component -->
<template>
    <!-- 반드시 Template 안에는 단 1개의 최상단 태그(노드)) -->
    <div>
        <h1>나쁜 말 거름</h1>
        <input type="text" v-model="input">
        <p>{{filteredInput}}</p>
        <div class="static" v-bind:class="{ acitive: isActive, error: hasError }">Hi</div>
    </div>
</template>

<script>
/* eslint-disable no-console */
export default {
    name: 'App',
    // 왜인지는 모르겠지만, 이제부터는 data를 function으로 만들어야 해
    data: function () {
        return {input: '',
            isActive: true,
            hasError: false,
        }
    },
    methods: {},
    computed: {
        filteredInput: function () {
            return `${this.input.replace(/바보|멍청이|똥개/gi, '**')}`;
            // g : 전체 모든 열을 변경
            // i : 대/소문자 구분 안하겠다.
            }
        }
    }
</script>

<style>
.isActive {
    color:aqua;
}

.hasError {
    background-color: blueviolet;
}
</style>