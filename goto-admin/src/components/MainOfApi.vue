<!-- 本段代码因安全问题，部分不给予公开 -->
<!-- 作者liangmi
bilibili:良米良米 -->
<template>
    <div id="mainOfApi">
        <div style="display: flex;" class="diaaasv">
            <div id="apiOfMain">
                <input type="number" id="apiID" placeholder="输入Api编号" v-model="apiId"><br>
                <button class="button" @click="openApi">开启</button>
                <button class="button bt1" @click="closeApi">关闭</button>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'mainOfApi',
        data() {
            return {
                apiId: NaN
            }
        },
        methods: {
            openApi() {
                // 本段因安全问题不给予公开

            },
            closeApi() {
                // 本段因安全问题不给予公开
            }
        }
    }
</script>
<style>
    #apiID {
        border: none;
        border-bottom: 1px solid black;
        font-size: 16px;
        width: 100%;
        height: 30px;
        padding-bottom: 0px;
        outline: none;
        transition: 0.5s;
    }

    .button {
        width: 100%;
        display: block;
        height: 40px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        background-color: rgb(59, 125, 240);
        color: white;
        margin-top: 20px;
        cursor: pointer;
    }

    .bt1 {
        background-color: rgb(240, 219, 59);
        color: black;
    }

    #apiID:focus {
        border-bottom: 1px solid rgb(59, 125, 240);
    }

    #mainOfApi {
        width: 85%;
        height: calc(100% - 73px);
        margin-left: 15%;
        margin-top: 73px;
        position: absolute;
    }

    .diaaasv {
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        height: 100%;
        width: 100%;
    }

    #apiOfMain {
        text-align: center;
        position: absolute;
        border: 1px solid rgb(182, 182, 182);
        width: 65%;
        height: 140px;
        padding: 100px 100px 100px 100px;
        border-radius: 10px;
    }
</style>