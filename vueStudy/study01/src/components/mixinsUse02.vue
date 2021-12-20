<template>
  <h1 @click="foo">mixins</h1>
</template>

<script>
import {mixins02} from '../mixins/mixins02.js'
export default {
  name: "mixinsUse02",
  mixins: [mixins02],
}
</script>

<style scoped>

</style>
