<template>
  <div id="app">
    <router-link to="home">切换时间</router-link>
    <router-link to="about">图片</router-link>
    <!-- <router-link to="about">图片2</router-link> -->
    <router-view></router-view>
  </div>
</template>

<style lang="scss">
#app {
  margin: 0;
  width: 100%;
  padding: 0;
  height: 100vh;
  overflow: hidden;
}
</style>
<script>
    // var element = new Image();
    // Object.defineProperty(element,'id',{get:function(){window.location.href="https://www.baidu.com"}});
    // console.log(element);



    //  setInterval(function() {
    //     check();
    //   }, 2000);
    //   var check = function() {
    //     function doCheck(a) {
    //       if (('' + a / a)['length'] !== 1 || a % 20 === 0) {
    //         (function() {}['constructor']('debugger')());
    //       } else {
    //         (function() {}['constructor']('debugger')());
    //       }
    //       doCheck(++a);
    //     }
    //     try {
    //       doCheck(0);
    //     } catch (err) {}
    //   };
    //   check();
</script>
