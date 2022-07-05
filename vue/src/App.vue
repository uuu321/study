<template>
  <van-notice-bar
      left-icon="volume-o"
      text="主要按钮成功按钮默认按钮警告按钮危险按钮主要按钮成功按钮默认按钮警告按钮危险按钮主要按钮成功按钮默认按钮警告按钮危险按钮"
  />


  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <van-button type="primary">主要按钮</van-button>
  <van-button type="success">成功按钮</van-button>
  <van-button type="default">默认按钮</van-button>
  <van-button type="warning">警告按钮</van-button>
  <van-button type="danger">危险按钮</van-button>


</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import { createApp } from 'vue';
import { Button,NoticeBar } from 'vant';
const app = createApp();
app.use(Button,NoticeBar);
export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
