<template>
  <div class="html">
    <div class="header">
      <div class="nav">
      <Menu></Menu>
      </div>
    <div class="text">
      <h1>欢迎来到，叶春亭的个人博客</h1>
      <h2>slogen</h2>
    </div>
    </div>
  <button @click="test">http://localhost:8001http://localhost:8001</button>
  </div>
</template>

<script>
import request from '../axios/index'
import Menu from '../components/Menu.vue'
import axios from 'axios'
export default {
    name:'Index',
    components:{
      Menu
    },
    data() {
      return {
        info:{},
        value:false
      }
    },
    watch:{
      value(val){
        if(val){
          //开启自动打卡
          this.run()
        }
      }
    },
    computed:{
      
    },
    methods:{
      test(){
        
      }
    }
}
</script>

<style scoped>
  .html{
    display: flex;
    flex-direction: column;
  }

  .header{
    display: flex;
    background-image: url('../assets/img/index/4.jpg');
    background-size: 100%;
    background-position: center;
    flex-direction: column;
    height:712px;
  }
    .nav{
    width: 100%;
    position: fixed;
    flex-grow: 0;
  }
  .text{
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: rgb(221, 218, 230);
  }
</style>