<template>
  <div class="user">
      <h1>{{dataUser.msg}}</h1>
<!--      这里可以通过$route.params.name来获取路由的参数-->
      <p v-if="$route.params.id">(param)欢迎回来,{{$route.params.name}}</p>
      <p v-if="$route.query.id">（query)欢迎回来,{{$route.query.name}}</p>

      <button @click="showView">get</button>
      <div v-if="showData">
        <p v-if="dataUser.params.id">params:{{dataUser.params}}</p>
        <p v-if="dataUser.query.id">query:{{dataUser.query}}</p>
      </div>

  </div>
</template>

<script>

export default {
  name: "user",
  data () {
    return {
      dataUser: {
        msg: 'Hello User!',
        params: {},
        query: {}
      },
      showData: false
    }
  },

  mounted(){
    this.dataUser.params = this.$route.params
    this.dataUser.query = this.$route.query
    console.log("m-p",this.$route.params)
    console.log("m-q",this.$route.query)
    console.log("m",this.dataUser)
    console.log("m-this",this)
  },

  updated(){
    console.log("up",this.dataUser)
    console.log("up-this",this.$data)
  },

  methods:{
    showView(){
      this.showData = true
    }

  },

}
</script>

<style scoped>

</style>
