<!-- 作者良米bilibili:良米良米 -->
<template>
    <button id="btn" @click="$emit('click')">{{ innerHtml }}</button>
</template>
<script>
    export default {
        name: 'titleBtn',
        props: {
            innerHtml: String
        },

    }
</script>
<style>
    #btn {
        height: 33px;
        border: none;
        font-size: 18px;
        padding: 0px 13px 0px 13px;
        background: none;
        color: white;
        transition: 0.1s;
    }
</style>