<template>

</template>

<script>
import { myMixins } from "../mixins/myMixins.js";
export default {
  name: "mixinsUse",

  mixins: [myMixins],
  data () {
    return {
      data1: 'index1',
      data3: 'index3'
    }
  },
  computed: {
    computed1 () {
      return this.data1 + this.data2
    },
    computed3 () {
      return this.data2 + this.data3
    }
  },
  mounted () {
    console.log('组件中的mounted')
    this.handleMethod1()
    this.handleMethod2()
    this.handleMethod3()
  },
  methods: {
    handleMethod1 () {
      console.log(
        `组件中的方法1，
        data1：${this.data1}，
        computed1：${this.computed1}`
      )
    },
    handleMethod3 () {
      console.log(
        `组件中的方法3，
        data3：${this.data3}，
        computed3：${this.computed3}`
      )
    }
  }

}
</script>

<style scoped>

</style>
