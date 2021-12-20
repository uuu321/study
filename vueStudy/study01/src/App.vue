<template>
  <div id="app">
    <img src="./assets/logo.png">
    <div>
      <mixinsUse></mixinsUse>
      <mixinsUse02></mixinsUse02>
    </div>
    <div>
      <router-link to>
        <button @click="$router.back(-1)">返回</button>
      </router-link>
    </div>
<!--    router-link定义页面中点击触发部分-->
    <div>
      <router-link :to="{path:'/'}">indexPath</router-link>
      <router-link :to="{name:'HelloWorld'}">indexName</router-link>
      <router-link :to="{path:'/first'}">First</router-link>
      <router-link :to="{path:'/empty1'}">Empty1</router-link>
      <router-link :to="{path:'/empty2'}">Empty2</router-link>
    </div>
<!--    动态路由-->
    <router-link :to="{path:'/UserQuery',query:{name:'user1',id:'1',sex:'女'}}">动态路由1</router-link>
    <router-link :to="{path:'/UserQuery',query:{name:'user2',id:'2',sex:'男'}}">动态路由2</router-link>
    <router-link :to="{name:'UserParam',params:{name:'user3',id:'3',sex:'男'}}">动态路由3</router-link>
<!--    router-view定义页面中显示部分-->
    <router-view :key="$route.fullPath"/>
  </div>
</template>

<script>
import mixinsUse from './components/mixinsUse.vue'
import mixinsUse02 from './components/mixinsUse02.vue'

export default {
  name: 'App',
  components: {mixinsUse,mixinsUse02},
  methods:{

  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
