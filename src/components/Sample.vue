<template>
  <div class="articles">
    <label v-for="article in articles" :key=article.title>
      <Box :title="article.title"/>
    </label>
  </div>
</template>

<script lang="ts">
import Box from '@/components/Box.vue'
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component({
  components: {
    Box
  }

})
export default class articles extends Vue {
  articles=[
    {title:"Sample Article"}, {title:"Sample Article2"}, {title:"Sample Article3"}
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
