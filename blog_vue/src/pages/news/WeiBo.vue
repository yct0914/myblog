<template>
  <div class="body">
      <!--循环渲染新闻列表-->
      <NewsHeader/>
      <el-divider></el-divider>
    <div class="main">
      <div class="item" v-for="n in news" :key="n.title">   
        <div class="rank" v-if="n.rank == 0">
            <img src="../../assets/img/news/hotRank1.png">
            <h2 class="rank">{{n.rank+1}}</h2>
        </div>
        <div class="rank" v-else-if="n.rank == 1">
            <img src="../../assets/img/news/hotRank2.png">
            <h2 class="rank">{{n.rank+1}}</h2>
        </div>
        <div class="rank" v-else-if="n.rank == 2">
            <img src="../../assets/img/news/hotRank3.png">
            <h2 class="rank">{{n.rank+1}}</h2>
        </div> 
        <div class="rank-default" v-else-if="n.rank > 2&&n.rank <9">
            <img src="../../assets/img/news/hotRankDefault.png">
            <h2 class="rank">{{n.rank+1}}</h2>
        </div>
        <div class="rankD" v-else>
            <img src="../../assets/img/news/hotRankDefault.png">
            <h2 class="rankD">{{n.rank+1}}</h2>
        </div>
        <div class="title">
            <h5>{{n.title}}</h5>
        </div>
        <div class="hot">
            <h5>{{n.hotNum}}</h5>
            <img src="../../assets/img/news/fire.webp">
        </div>
        </div>
    </div>
  </div>
</template>

<script>
import request from '../../axios/index'
import NewsHeader from '../../components/News/NewsHeader.vue'
export default {
    name:'WeiBo',
    data() {
        return {
            news:[],
            
        }
    },
    components:{
      NewsHeader  
    },
    mounted(){
        request('/news/weibo').then(data => {
            this.news = data
        },
        error => {
            this.$message({
                type:'error',
                message:'数据获取失败'
            })
        }
        )
        //刷新新闻
        this.$bus.$on('updateNews',this.updateNews)
    },
        beforeDestroy(){
        //销毁全局事件
        this.$bus.$off('updateNews')
    },
    methods:{
        updateNews(){
            request('/news/weibo').then(data => {
            this.news = data
            this.$message({
                type:'success',
                message:'刷新成功!'
            })
            },
            error => {
                this.$message({
                    type:'error',
                    message:'数据获取失败'
                })
            }
            )
        }
    }
}
</script>

<style scoped>
    .body{
        display: flex;
        flex-direction: column;
        border-bottom-right-radius: 10px;
    }


    .main{
        display: flex;
        flex-direction: column;
        flex-grow: 1;
        border-bottom-right-radius: 10px;
    }
    .item{
        display: flex;
        flex-direction: row;
        height: 70px;
        align-items: center;
        border-top-right-radius: 10px;
        border-radius: 10px;
        transition: 0.5s;  
        cursor: pointer;      
    }
    .item:hover{
        background-color:antiquewhite;
    }
    .rank img{
        position: absolute;
        z-index: 1;
        top: 8px;
    }
    .rank-default img{
        position: absolute;
        z-index: 1;
        top: 17px;
        left: 25px;
    }
    .rankD img{
        position: absolute;
        z-index: 1;
        top: 17px;
        left: 25px;
    }
    .rank-default,.rank{
        position: relative;
        width: 100px;
        justify-content: center;
    }
    .rankD{
        position: relative;
        width: 100px;
        justify-content: center;
    }
    h2.rank{
        position: relative;
        z-index: 100;
        left: 50px;
    }
    h2.rank-default{
        position: relative;
        z-index: 100;
        left: 50px;
    }
    h2.rankD{
        position: relative;
        z-index: 100;
        left: 40px;
        margin-right: 20px;
    }
    .title{
        font-size: 30px;
        width: 90%;
    }
    .hot{
        display: flex;
        align-items: center;
        margin-right: 5px;
    }
    .hot img{
        width: 20px;
        height: 33.13px;
    }

</style>