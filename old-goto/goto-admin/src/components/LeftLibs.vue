<!-- 作者：liangmi bilibili:良米良米 -->
<template>
    <div id="leftLib">
        <button class="active oneLib" @click="toggleLink" ref="link"><i class="fa fa-globe"></i>
            链接管理</button>
        <button class="oneLib" @click="toggleApi" ref="api"><i class="fa fa-globe"></i>
            Api管理</button>
        <div id="row">
        </div>
    </div>
</template>
<script>
    export default {
        name: "LeftLibs",
        methods: {
            toggleApi() {
                // this.$emit('switch-to-api')
                // this.$parent.toApi();
                this.$refs.api.classList.add("active");
                this.$refs.link.classList.remove("active");
                this.$parent.toApi();
            },
            toggleLink() {
                // this.$emit('switch-to-link');

                this.$refs.api.classList.remove("active");
                this.$refs.link.classList.add("active");
                this.$parent.toLink();
            },
            exitBs() {

                fetch("https://go.sunzishaokao.com/api/delete/auth", {
                    method: "GET",
                    headers: {
                        label: "admin_" + this.$cookies.get("username")
                    }
                })
                this.$cookies.set('username', '', -1);
                this.$cookies.set('token', '', -1);
                window.close()
            }
        },
    }
</script>
<style>
    #row {
        height: 100%;
        width: 1px;
        background-color: rgb(137, 137, 137);
        position: absolute;
        left: 100%;
        top: 0;
    }

    #exit1 {
        color: black;
    }

    #leftLib {
        width: 15%;
        height: calc(100% - 73px);
        margin-top: 73px;
        position: absolute;
    }

    #exit {
        border: none;
        height: 35px;
        background-color: rgb(255, 197, 111);
        font-size: 16px;
        cursor: pointer;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
        position: absolute;
    }

    .oneLib {
        height: 50px;
        width: 100%;
        padding-left: 25px;
        text-align: left;
        border: 3px solid rgb(227, 227, 227);
        border-top: none;
        border-right: none;
        border-left: none;
        background: none;
        outline: none;
        font-size: 16px;
        cursor: pointer;
    }

    .active {
        background-color: rgba(0, 0, 0, 0.187);
    }

    .fa {
        color: cadetblue;
    }
</style>