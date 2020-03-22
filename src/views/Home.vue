<template>
  <div class="home">
    <img alt="title-logo" src="../assets/title.png" width="200" height="200">
    <h1>Graphical Survey</h1>
    <Sample/>
  </div>
</template>

<script>
// @ is an alias to /src
import Sample from '@/components/Sample.vue'

export default {
  name: 'Home',
  components: {
    Sample
  }
}
</script>
