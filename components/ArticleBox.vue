<template>
    <div class="box">
        <p>{{ article.title }}</p>
        <i class="author">
          {{ article.author }}
        </i>
    </div>
</template>

<script>
export default {
    props: {
        article: {
            type: Object,
            required: true
        }
    },
    data(){
        return {
            count: 0
        };
    },
    methods: {
    },
}
</script>

<style scoped>
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