<template>
  <div class="html">
    <div class="header">
      <div class="header-nav">
      <Menu></Menu>
      </div>
      <div class="text">
        <h1>今日热搜</h1>
        <h2>发现新世界</h2>
      </div>
    </div>
    <div class="body">
      <div class="main">
        <div class="nav">
          <NewsNav/>
        </div>
        <el-divider direction="vertical"></el-divider>
          <div class="news-main">
          <router-view></router-view>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import Menu from '../components/Menu.vue'
import NewsNav from '../components/News/NewsNav.vue'
import router from '../router/index.js'
// router.beforeEach(
//   (to,from,next) => {
//     if(to.name == 'news'){
//       return {name:'weibo',replace:true}
//     }
//   }
// )
export default {
  name: 'News',
  components:{
    Menu,
    NewsNav
  },
  methods:{

  },

}
</script>

<style scoped>
  .html{
    display: flex;
    flex-direction: column;
  }
  .header{
    display: flex;
    background-image: url('../assets/img/news/header.jpeg');
    background-size: 100%;
    background-position: center;
    flex-direction: column;
    height:712px;
  }
  .header-nav{
    width: 100%;
    position: fixed;
  }
  .text{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-grow: 1;
    color: rgb(47, 38, 66);
  }
  .text h1{
    justify-content: center;
    font-size: 50px;
    margin-bottom: 5px;

  }
  .text h2{
    font-size: 30px;  
  }
  .body{
    display: flex;
  }
  .main{
    border-radius: 10px;
    display: flex;
    width: 80%;
    height: auto;
    margin-top: 20px;
    margin-left: 10%;
    margin-right: 10%;
    box-shadow: 0 20px 60px 0 rgb(0 0 0 / 40%);
  }
  .nav{
    display: flex;
    width: 15%;
    /* background-color: aquamarine; */
  }
   .news-main{
    border-bottom-right-radius: 10px;
    display: flex;
    flex-direction: column;
    width: 85%;
  }/*
  .news-header{
    flex-grow: 0;
    height: 100px;
    border-top-right-radius: 10px;
  }
  .news{
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    border-bottom-right-radius: 10px;
  } */
  .el-divider--vertical{
    height: 100%;
    margin: 0;
  }
</style>