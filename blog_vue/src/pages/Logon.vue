<template>
  <div class="body">
      <img src="../assets/img/logon/1.svg" alt= "left" class="left">
      <img src="../assets/img/logon/2.svg" alt="right" class="right">
      <div class="main">
          <div class="image">
              <nav>
                <router-link to="/index" active-class="active">主页</router-link>
                <router-link to="/news" active-class="active">新闻</router-link>
                <router-link to="/news" active-class="active">新闻</router-link>
                <router-link to="/news" active-class="active">新闻</router-link>
                <router-link to="/login" active-class="active">注册</router-link>
        </nav>
          </div>
        <div class="logon">
            <header>
          <h1>登录</h1>
          <el-divider>
            <i class="el-icon-s-promotion"></i>
          </el-divider>
          <div>
            还没有账号? <router-link to="/login">点击注册</router-link>
          </div>
            </header>
            <el-form :model="userInfo" status-icon :rules="rules" ref="userInfo" label-width="100px" class="demo-ruleForm" size="medium">
            <el-form-item label="用户名" prop="username">
                <el-input type="text" v-model="userInfo.username"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input :type="passwordType" v-model="userInfo.password" autocomplete="off">
                    <i slot="suffix" class="el-icon-view" id="i" @click="showPass"></i>
                </el-input>
            </el-form-item>
            
            <el-form-item label="验证码" prop="code">
                <el-input type="text" v-model="userInfo.code" placeholder="单击图片生成验证码"></el-input>
                <div @click="refreshCode" class="identify">
                    <SIdentify :identifyCode="identifyCode"></SIdentify>
                </div>
            </el-form-item>
            <el-form-item>
                <div class="check">
                    <el-checkbox>记住我</el-checkbox>
                </div>
                <div class="button">
                    <el-button @click="logon('userInfo')" type="success" icon="el-icon-s-promotion">登录</el-button>
                </div>
            </el-form-item>
        </el-form>
        <footer>
            <el-divider>
                其他登录方式
            </el-divider>
        </footer>
        </div>
      </div>
  </div>
</template>

<script>
import request from '../axios/index'
import SIdentify from '../components/Logon/SIdentify'
export default {
    name:'Logon',
    components:{
        SIdentify
    },
    data() {
        return {
            passwordType: 'password',
            identifyCodes:'0123456789qwertyuiopasdfghjklzxcvbnm',
            identifyCode: '',
            userInfo:{
                code: '',
                username: '',
                //password: ''
            },
            rules:{
                username:[
                    {required: true, message: '请输入用户名', trigger: 'blur'}
                ],
                password:[
                    {required: true, message: '请输入密码', trigger: 'blur'}
                ],
                code:[
                    {required: true, message: '请输入验证码', trigger: 'blur'}
                ]
            }
        }
    },
    methods:{
        logon(formName){
            this.$refs[formName].validate(valid => {
                if(valid){
                    //验证码的校验
                    if(this.userInfo.code !== this.identifyCode){
                        this.$message({
                            message:'验证码错误!',
                            type:'error'
                        })
                        this.userInfo.code = ''
                        return false
                    }
                    //向服务端发请求校验用户名和密码
                    request('/user/logon', 'POST', this.userInfo).then(response => {
                        this.logonChange()
                        this.$message({
                            message:'登录成功!3s后跳转至主页',
                            type: 'success'
                        })
                        setTimeout(() => {
                          this.$router.push({name:'index'})
                        },3000)
                    },
                    error => {
                        if(error.data == 'error'){
                            this.$message({
                                message:'用户名或密码错误!',
                                type:'error'
                            })
                            this.$refs[formName].resetFileds()
                        }
                        else{
                            this.$message({
                                message:'服务器无响应',
                                type: 'error'
                            })
                            this.$refs[formName].resetFileds()
                        }
                    }
                    )
                }
                else{
                    return false
                }
            })
        },
         // 验证码处理
    randomNum(min, max) {
      return Math.floor(Math.random() * (max - min) + min)
    },

    // 刷新验证码
    refreshCode() {
      this.identifyCode = ''
      this.makeCode(this.identifyCodes, 4)
    },
    makeCode(o, l) {
      for (let i = 0; i < l; i++) {
        this.identifyCode += this.identifyCodes[
          this.randomNum(0, this.identifyCodes.length)
        ]
      }
    },
    showPass(){
        this.passwordType === 'password' ? this.passwordType = 'text' : this.passwordType = 'password';
        let e = document.getElementById('i');
        this.passwordType == 'text' ? e.setAttribute('style', 'color: #409EFF') : e.setAttribute('style', 'color: #c0c4cc');
      },
    logonChange(){
      this.$root.isLogon = !this.$root.isLogon
    }

    }
}
</script>

<style scoped>
    
  .body{
    height: auto;
    position: relative;
  }
   .left{
    position: relative;
    width: 400px;
    top: 300px;
    left: 20px;
  }
  .right{
    position: relative;
    width: 400px;
    top: 300px;
    right: -700px;
    
  } 
  .main{
    display: flex;
    width: 1000px;
    height: 570px;
    top: 19%;
    left: 17%;
    position: absolute;
    background-color: white;
    box-shadow: 0 20px 80px 0 rgb(0 0 0 / 30%);

  }
  .image{
    background-image: url('../assets/img/logon/1.1.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    height: 570px;
    width: 50%;
 
  }
  .logon{
    display: flex;
    flex-direction: column;
    width: 440px;
    justify-content: center;
    padding: 60px;
    font-size: 14px;
    margin: 0px;

  }
  header{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    align-content: center;
    margin-bottom: 20px;
  }
  a{
    text-decoration: none;
    color: rgb(91, 145, 155);
  }
  a:hover{
    color: rgb(200, 255, 127);
  }
  label{
    text-align: center;
  }
  .identify{
      margin-top: 20px;
      width: 200px;
  }
  canvas{
      width: 200px;
  }
  .check{
      display: flex;
      justify-content: flex-start;
  }
  .button{
      display: flex;
      justify-content: center;
  }
  nav{
    display: flex;
    height: 50px;
    line-height: 50px;
    width: 100%;
    background-color: rgba(212, 171, 216,0.1);
  }
  nav a{
    color:rgb(34, 98, 71);
    flex-grow: 1;
    width: 30px;
    text-align: center;
    transition: 0.3s;
  }
  nav a:hover{
    background-color: rgba(211, 172, 202,0.3);
  }
</style>