<!-- 
  作者：良米
  bilibili:良米良米
 -->
<template>
  <div id="app">
    <AppBar></AppBar>
    <LeftLibs @swich-to-link="toLink()" @swich-to-api="toApi()"></LeftLibs>
    <MainOfLink :class="linkClass"></MainOfLink>
    <MainOfApi :class="apiClass"></MainOfApi>
  </div>
</template>

<script>
  import AppBar from "./components/AppBar.vue"
  import LeftLibs from "./components/LeftLibs"
  import MainOfLink from "./components/MainOfLink.vue"
  import MainOfApi from "./components/MainOfApi.vue"


  export default {
    name: 'App',
    components: {
      AppBar,
      LeftLibs,
      MainOfLink,
      MainOfApi
    },
    data() {
      return {
        linkClass: "",
        apiClass: "invis"
      }
    },
    mounted() {
      //全局Js写在这里
      console.log(this.$cookies.get('username'))
      if (this.$cookies.get('username') == null) {
        window.location.href = "./login.html";
      }
      setTimeout(() => {
        location.reload();
      }, 3600000)
    },
    methods: {
      toLink() {
        // this.$refs.links.classList.remove("invis");
        // this.$refs.apis.classList.add("invis");
        this.linkClass = "";
        this.apiClass = "invis"
      },

      toApi() {
        // this.$refs.links.classList.add("invis");
        // this.$refs.apis.classList.remove("invis");
        this.linkClass = "invis";
        this.apiClass = "";
      }
    }
  }
</script>
<style>
  .invis {
    display: none;
  }

  #app {
    height: 100%;
  }
</style>