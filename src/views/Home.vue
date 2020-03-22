<template>
  <div class="home">
    <img alt="title-logo" src="../assets/title.png" width="200" height="200">
    <h1>Graphical Survey</h1>
    <ArticleView/>
  </div>
</template>

<script>
// @ is an alias to /src
import ArticleView from '@/components/ArticleView.vue'

export default {
  name: 'Home',
  components: {
    ArticleView
  }
}
</script>
