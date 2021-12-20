export const mixins02 = {
  data () {
    return {
      data1: 'mixin1',
      data2: 'mixin2'
    }
  },
  methods:{
    foo(){
      console.log('a',this.data1 + this.data2)
    }
  }
}
