<!-- 作者良米bilibili:良米良米 -->
<template>
    <div id="bar">
        <span id="title">GoTo管理控制台</span>
        <span id="secTitle">go.sunzishaokao.com</span>
        <titleBtn innerHtml="GoTo管理控制台" />
        <!-- <LoginOrRegister loginStates="true"></LoginOrRegister> -->
        <LoginOrRegister loginStates userHeadImg="favicon.ico"></LoginOrRegister>
    </div>
</template>
<script>
    import titleBtn from "./titleBtn.vue";
    import LoginOrRegister from "./LoginOrRegister.vue"
    export default {
        name: 'AppBar',
        methods: {
            goHome() {
                alert("这个功能还没写完捏")
            },
            accountMg() {
                alert("这个功能还没写完捏")
            },
            resSearch() {
                alert("这个功能还没写完捏")
            },
            makeQtn() {
                alert("这个功能还没写完捏")
            }
        },
        components: {
            titleBtn,
            LoginOrRegister
        }
    }

</script>
<style>
    #bar {
        background-color: rgb(21, 127, 248);
        width: 100%;
        height: 33px;
        padding-top: 20px;
        padding-bottom: 20px;
        box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.581);
        color: rgb(255, 242, 202);
        position: fixed;
        top: 0;
        margin-top: 0;
    }

    #title {
        margin-left: 100px;
        margin-right: 20px;
        line-height: 28px;
        font-size: 28px;
        font-weight: 400;
    }

    #secTitle {
        position: absolute;
        top: 48px;
        left: 100px;
        font-size: 5px;
        margin-left: 3px;
    }
</style>