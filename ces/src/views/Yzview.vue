
<template>
  <div id="app">
    <div class="nav-box">
      <input type="text" v-model="hr" placeholder="环绕文字" />
      <input type="text" v-model="xh" placeholder="底部文字" />
      <button @click="chapter">生成</button>
      <button @click="reset">清除</button>
    </div>

    <canvas id="canvas" width="200" height="200"></canvas>
  </div>
</template>

<script>
import chapter from "./chapter/chapter";
export default {
  data() {
    return {
      hr: "",
      xh: "",
    
    };
  },
  methods: {
    chapter() {
      chapter(this.xh, this.hr);
      console.log(this.xh);
    },
    reset(){
      console.log("asda")
      this.hr=""
      let canvas = document.getElementById("canvas");
      canvas.height=canvas.height;
    }
  }
};
</script>

<style>
#app {
  margin: 0;
  padding: 0;
  text-align: center;
}
.nav-box {
  width: 100%;
  height: 100px;
}
#canvas {
  background-color: transparent;
}
</style>

