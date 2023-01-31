<template>
  <div id="app">
    <AppBar></AppBar>
    <NextLink></NextLink>
    <TextOfMain></TextOfMain>
    <AppFooter></AppFooter>

  </div>
</template>

<script>
  import AppBar from "./components/AppBar.vue"
  import AppFooter from "./components/AppFooter.vue"
  import NextLink from "./components/NextLink.vue"
  import TextOfMain from './components/TextOfMain.vue'

  export default {
    name: 'App',
    components: {
      AppBar,
      AppFooter,
      NextLink,
      TextOfMain
    },
  }
</script>
<style>
  * {
    margin: 0;
    padding: 0;
  }

  #app {
    width: 100%;
    height: 100%;
    /* display: flex; */
  }
</style>