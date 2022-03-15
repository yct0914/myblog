<template>
  <div class="body">
      <div class="text">
          <h2>热搜网站</h2>
      </div>
      <el-divider></el-divider>
      <div class="item" @click="weibo"> 
              <img src="../../assets/img/news/weibo.png" alt="">
          <div class="news-name">
              <h2>微博</h2>
          </div>
      </div>
  </div>
</template>

<script>
export default {
    name: 'NewsNav',
    methods:{
        weibo(){
            this.$router.push({name:'weibo'})
        }
    }
}
</script>

<style scoped>
    .body{
        display: flex;
        flex-direction: column;
        width: 100%;

    }
    .text{
        display: flex;
        height: 100px;
        justify-content: center;
        align-items: center;
    }
    .item{
        width: 100%;
        display: flex;
        flex-direction: row;
        height: 70px;
        justify-content: center;
        align-items: center;
        cursor:pointer;
        transition: 0.5s;
        border-radius: 10px;
    }
    .item:hover{
        background-color: blanchedalmond;
    }
    /* .item .logo{
        height: 50px;
        width: 50px;
        background-image: url('../../assets/img/news/weibo.png');
        background-position: center;
        background-clip: content-box;
    } */
    .item img{
        display: block;
        width: 40px;
        height: 40px;
        margin-left: 10px;
        flex-grow: 0;

    }
    .item .news-name{
        flex-grow: 1;
        text-align: center;
}
</style>