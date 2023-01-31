<!-- 作者：良米bilibili:良米良米 -->
<template>
    <div id="mainOfLink">
        <!-- 添加链接 -->
        <div id="linkList">
            <h3 style="margin-left:30px;margin-top: 30px;">添加新的链接:</h3>
            <form @submit.prevent="onSubmit" style="margin: 30px;">
                <input type="text" class="input" v-model="link">
                <button type="submit" id="submitLink">提交</button>
            </form>

            <!-- 列表 -->
            <ul>
                <li v-for="(link1,index) in link1s" :key="link1.ID" ref="li"
                    :class="{ 'first': index === 0, 'last': index === link1s.length - 1 }">
                    <span class="statusLink id" style="margin-right: 5px;">{{ link1.ID }}</span>
                    <span class="url">{{ link1.url }}</span>
                    <span class="statusLink">{{ link1.zh_status }}</span>
                    <button style="margin-left:5px;border:none;border-radius: 2px;height: 22.5px;cursor: pointer;"
                        @click="getHit(index)">获取命中数</button>
                    <span class="hit"> 命中次数：未获取</span>
                    <span class="control">
                        <i class="fa fa-xmark cross" @click="delLink(index)" title="强制删除" style="cursor: pointer;"></i>
                        |
                        <i class="fa fa-check check" @click="changeLink('pass',index)" title="通过审核"
                            style="cursor: pointer;"></i> |
                        <span class="updataLink" @click="changeLink('sub',index)">强制上线</span> |
                        <span class="cancelLink" @click="changeLink('cancel',index)">取消链接</span>
                    </span>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                link: '',
                link1s: [],
                noCheckLink1s: [],
                filterText: ""
            }
        },
        name: 'mainOfLink',
        computed: {
            link11s() {
                return this.link1s.filter(link1 => link1.name.toLowerCase().includes(this.filterText.toLowerCase()))
            }
        },
        methods: {
            delLink(index) {
                fetch("https://go.sunzishaokao.com/api/delete", {
                    // fetch("https://go.limenoon.com/api/delete", {
                    method: "DELETE",
                    headers: {
                        'Content-Type': 'application/json',
                        'label': "admin_" + this.$cookies.get('username'),
                        'token': this.$cookies.get('token'),
                    },
                    body: JSON.stringify({ url: this.$el.querySelectorAll('.url')[index].innerHTML })
                }).then(res => res.json()).then(data => {
                    if (data.error) {
                        alert("出现错误！" + data.error)
                    } else {
                        fetch('https://go.sunzishaokao.com/api/get/data', {
                            // fetch('https://go.limenoon.com/api/get/data', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'label': "admin_" + this.$cookies.get('username'),
                                'token': this.$cookies.get('token')
                            }

                        }).then(res => res.json()).then(data => {
                            if (data.status == 200) {
                                this.link1s = data.data
                            } else {
                                alert("请求失败！" + data.error + "请重载网页！");
                            }
                        })
                    }
                })
            },


            async onSubmit() {
                // const respsonse = await fetch('/api/send-message', {
                await fetch('https://go.sunzishaokao.com/api/submit/robot', {
                    // await fetch('https://go.limenoon.com/api/submit/robot', {
                    method: 'POST',
                    body: JSON.stringify({ url: this.link, mode: "admin" }),
                    headers: {
                        'Content-Type': 'application/json',
                        'label': "admin_" + this.$cookies.get('username'),
                        'token': this.$cookies.get('token')
                    }
                }).then(res => res.json()).then(data => {
                    if (data.status == 200) {
                        // 将列表刷新
                        fetch('https://go.sunzishaokao.com/api/get/data', {
                            // fetch('https://go.limenoon.com/api/get/data', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'label': "admin_" + this.$cookies.get('username'),
                                'token': this.$cookies.get('token')
                            }

                        }).then(res => res.json()).then(data => {
                            if (data.status == 200) {
                                this.link1s = data.data
                            } else {
                                alert("请求失败！" + data.error + "请重载网页！");
                            }
                        })
                    } else {
                        alert(data.message)
                    }
                });
            },

            changeLink(mod, index) {
                fetch('https://go.sunzishaokao.com/api/change/data', {
                    // fetch('https://go.limenoon.com/api/change/data', {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                        'label': "admin_" + this.$cookies.get('username'),
                        'token': this.$cookies.get('token')
                    },
                    body: JSON.stringify({ url: this.$el.querySelectorAll('.url')[index].innerHTML, mode: mod })
                }).then(res => res.json()).then(data => {
                    if (data.error) {
                        alert("发生错误！" + data.error)
                    } else {
                        fetch('https://go.sunzishaokao.com/api/get/data', {
                            // fetch('https://go.limenoon.com/api/get/data', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'label': "admin_" + this.$cookies.get('username'),
                                'token': this.$cookies.get('token')
                            }

                        }).then(res => res.json()).then(data => {
                            if (data.status == 200) {
                                this.link1s = data.data
                            } else {
                                alert("请求失败！" + data.error + "请重载网页！");
                            }
                        })
                    }
                }
                )
            },

            getHit(index) {
                console.log(`{'id':"` + this.$el.querySelectorAll('.id')[index].innerHTML + `"}`)
                fetch('https://go.sunzishaokao.com/api/get/data/cache', {
                    // fetch('https://go.limenoon.com/api/get/data/cache', {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        'label': "admin_" + this.$cookies.get('username'),
                        'token': this.$cookies.get('token')
                    },
                    body: `{"id":"` + this.$el.querySelectorAll('.id')[index].innerHTML + `"}`,
                }).then(res => res.json()).then(data => {
                    if (data.error == null) {
                        this.$el.querySelectorAll('.hit')[index].innerHTML = "命中次数：" + data.hit;
                    } else {
                        this.$el.querySelectorAll('.hit')[index].innerHTML = "命中次数：" + data.error;
                    }

                })
            }
        },
        created() {
            fetch('https://go.sunzishaokao.com/api/get/data', {
                // fetch('https://go.limenoon.com/api/get/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'label': "admin_" + this.$cookies.get('username'),
                    'token': this.$cookies.get('token')
                }

            }).then(res => res.json()).then(data => {
                if (data.status == 200) {
                    this.link1s = data.data
                } else {
                    alert("请求失败！" + data.error + "请重载网页！");
                }
            })
        },
    }
</script>
<style>
    .statusLink {
        background-color: rgb(234, 234, 234);
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 2px;
    }

    .cross {
        color: red;
    }

    #mainOfLink {
        width: 85%;
        margin-left: 15%;
        margin-top: 73px;
        position: absolute;
        height: auto;
    }

    #linkList {
        /* padding: 0px 30px 0px 30px; */
        margin: 50px auto;
        border: 1px solid rgb(182, 182, 182);
        border-radius: 10px;
        width: calc(80% + 60px);
    }

    .control {
        position: absolute;
        right: 15px;
    }

    .updataLink {
        color: rgb(33, 1, 122);
        cursor: pointer;
    }

    .cancelLink {
        color: rgb(33, 1, 122);
        cursor: pointer;
    }

    .scrc {
        margin-left: 30px;
        width: calc(100% - 75px);
        height: 25px;
        padding-left: 5px;
        margin-top: 0px;
        margin-bottom: 0px;
    }

    li {
        list-style: none;
        display: block;
        font-size: 16px;
        outline: 1px solid rgb(182, 182, 182);
        padding: 10px 0px 10px 0px;
        padding-left: 10px;
        width: (100% - 10px);
        left: 0px;
        position: relative;
    }

    .alter {
        margin-left: 5px;
        width: 52px;
    }

    li.first {
        margin-top: 30px;
    }

    li.last {
        border-radius: 0px 0px 10px 10px;
    }

    ul {
        margin: 0;
        padding: 0;
    }

    .input {
        border: none;
        outline: none;
        height: 20px;
        width: 90%;
        border-bottom: 1px solid black;
        font-size: 16px;
    }

    #submitLink {
        height: 35px;
        font-size: 16px;
        width: calc(10% - 15px);
        margin-left: 5px;
        border: none;
        border-radius: 5px;
        background-color: rgb(255, 225, 0);
        transition: 0.25s;
    }

    #submitLink:hover {
        box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);
    }
</style>