<template>
  <div>
    <div class="nav">
      <div class="left">
        <router-link to="/index" active-class="active">主页</router-link>
        <router-link to="/news" active-class="active">新闻</router-link>
        <router-link to="/news" active-class="active">新闻</router-link>
      </div>
      <div class="right" v-show="!this.$root.isLogon"> 
        <router-link to="/logon" active-class="active">登录</router-link>
        <router-link to="/login" active-class="active">注册</router-link>
      </div>
      <div class="right" v-show="this.$root.isLogon">
        <el-dropdown @command="select" @visible-change="drop">
          <span class="el-dropdown-link">
            下拉菜单<i class="el-icon-arrow-down el-icon--right" v-show="isDrop"></i>
            <i class="el-icon-arrow-left el-icon--right" v-show="!isDrop"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="self">个人中心</el-dropdown-item>
            <el-dropdown-item command="logout">注销</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name:'Menu',
    data() {
      return {
        isDrop:false
      }
    },
    methods:{
      drop(isDrop){
        this.isDrop = isDrop
      },
      select(command){
        if(command=='self'){
          this.$router.push({name:'self_info'})
        }
        else if(command=='logout'){
          console.log('logout!');
        }
      }
    }
}
</script>
<style scoped>
  .el-dropdown-link{
    color:rgb(47, 35, 56) ;
    cursor: pointer;
    font-size: 20px;
    transition: 0.5s;
  }
  .el-dropdown-link:hover{
    color: cadetblue;
  }
  .nav{
    height: 50px;
    line-height: 50px;
    display: flex;
    justify-content: space-between;
  }
  .left{
    display: flex;
    justify-content: left;
    margin-left: 50px;

  }
  .right{
    display: flex;
    justify-content: left;
    margin-right: 50px;
  }

  a{
    width: 40px;
    margin-left: 25px;
    margin-right: 25px;
    font-size: 20px;  
    text-decoration-line: none;
    transition: 0.3s;
    color:rgb(47, 35, 56) ;
  }
  a:hover{
    color: cadetblue;

  }
  .active{
    color: rgb(221, 127, 155);
  }
  
</style>>
