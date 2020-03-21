<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <Box title="Sample Article"/>
    <Box title="Sample Article2"/>
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
export default class Hello extends Vue {
  @Prop() private msg!: string;
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
