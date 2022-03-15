<template>
    <div class="header">
        <div class="title">
            <img src="../../assets/img/news/weibo.png">&nbsp;&nbsp;&nbsp;&nbsp;
            <h1>微博</h1>
        </div>
        <div class="update" @click="updateNews">
            <i class="el-icon-refresh">点击刷新</i>
        </div>
        
    </div>
</template>

<script>
export default {
    name:'NewsHeader',
    methods:{
        updateNews(){
            this.$bus.$emit('updateNews')
        }
    },
    
}
</script>

<style scoped>
    .header{
        display: flex;
        flex-direction: column;
        flex-grow: 0;
        height: 100px;
        border-top-right-radius: 10px;
        align-items: center;
        justify-content: center;
    }
    .title{
        display: flex;
        margin-top: 10px;
    }

    .title img{
        height: 80px;
        width: 80px;
    }
    .update{
        cursor: pointer;
        color: rgb(18, 15, 19);
        transition: 0.3s;
    }
    .update:hover{
        color: cadetblue;
    }
</style>