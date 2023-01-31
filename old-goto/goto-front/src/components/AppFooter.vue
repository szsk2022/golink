<template>
    <div>
        <div id="AppFooter" ref="AppFooter" style="bottom: 68px;">
            <h2 style="display: inline;margin: 0;">GoToLink</h2>
            <span class="tip">Tips:点击<span class="blod">后退</span>按钮可以再次GoTo</span>
        </div>

        <div id="IncAndIns" ref="IncAndIns">
            ©2022 GoToLink 版权所有
            <span class="footerButton" @click="gitee()">条款</span>
            <span class="footerButton" @click="gitee()">隐私</span>
            <a href="https://beian.miit.gov.cn" class="icp">鲁ICP备2022023454号-11</a>
            <img src="svg/github.svg" alt="GitHub" id="github" @click="gitee" style="cursor: pointer;">
        </div>
    </div>
</template>
<script>
    export default {
        name: "AppFooter",
        methods: {
            gitee() {
                window.open("https://gitee.com/szsk/golink");
            }
        },
        created() {
            this.$refs.AppFooter.style.bottom = this.$refs.IncAndIns.clientHeight;
        }
    }
</script>
<style>
    .icp {
        color: #8b949e;
        margin-left: 15px;
    }

    .tip {
        margin-left: 45%;
        color: #bbc6d3;
    }

    #github {
        margin-left: 50%;
    }

    #AppFooter {
        text-align: center;
        position: absolute;
        background-color: rgb(14, 17, 22);
        width: 100%;
        padding: 20px 0px 20px 0px;
        color: white;
    }

    .footerButton {
        margin-left: 15px;
        color: #8b949e;
        cursor: pointer;
    }

    #IncAndIns {
        position: absolute;
        bottom: 0px;
        text-align: center;
        background-color: rgb(23, 27, 33);
        padding: 20px 0px 20px 0px;
        color: rgb(202, 202, 202);
        width: 100%;
        font-size: 12px;
    }

    .blod {
        font-weight: bold;
    }
</style>