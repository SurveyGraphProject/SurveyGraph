<template>
    <div class="box">
        <p>{{ title }}</p>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class ArticleBox extends Vue {
  @Prop() private title!: string;
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.box{
    display: inline-block;
    border:1px solid black;
    width:100px;
    height:100px;
    text-align: center;
    margin: 10px;
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