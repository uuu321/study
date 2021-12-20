<template>
  <div class="first-app">
    {{msg}}
  </div>
</template>

<script>
export default {
  name: "First",
  data(){
    return {
      msg: "Welcome to FirstApp"
    };
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
