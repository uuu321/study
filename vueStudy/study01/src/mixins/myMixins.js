export const myMixins = {
  data () {
    return {
      data1: 'mixin1',
      data2: 'mixin2'
    }
  },
  computed: {
    computed1 () {
      return this.data1 + this.data2
    },
    computed2 () {
      return this.data1 + this.data3
    }
  },
  mounted () {
    console.log('mixin中的mounted')
  },
  methods: {
    handleMethod1 () {
      console.log(
        `mixin中的方法1，
        data1：${this.data1}，
        computed1：${this.computed1}`
      )
    },
    handleMethod2 () {
      console.log(
        `mixin中的方法2，
        data2：${this.data2}，
        computed2：${this.computed2}`
      )
    }
  }
}
