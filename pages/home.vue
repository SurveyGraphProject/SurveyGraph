<template>
    <div>
        <div v-for="article in ref" :key="article.id">
            <Article :article="article"/>
        </div>
    </div>
</template>

<script>
import Article from '~/components/ArticleBox.vue'
export default {
    components: {
    "Article": Article
    }, 
    data(){
        return {
            ref: [
                {title:"Sample Ref1", author:"yamada", year:2018, id: 0}, 
                {title:"Sample Ref2", author:"atom", year:2019, id: 1}, 
                {title:"Sample Ref3", author:"sakuma", year:2020, id: 2}
            ],
        }
    },
    methods: {
    }
}
</script>

<style scoped>

</style>