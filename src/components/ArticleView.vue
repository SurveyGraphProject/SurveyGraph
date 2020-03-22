<template>
  <div class="articles">
    <label v-for="article in articles" :key=article>
      <ArticleBox :article="article"/>
    </label>
  </div>
</template>

<script lang="ts">
import ArticleBox from '@/components/ArticleBox.vue'
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component({
  components: {
    ArticleBox
  }

})
export default class articles extends Vue {
  articles=[
    {title:"Sample Article", author:"yamada"}, {title:"Sample Article2", author:"atom"}, {title:"Sample Article3", author:"sakuma"}
  ];
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
