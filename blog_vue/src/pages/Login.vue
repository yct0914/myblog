
<template>
  <div class="body">
    <img src="../assets/img/login/1.svg" alt= "left" class="left">
    <img src="../assets/img/login/2.svg" alt="right" class="right">
    <div class="main">
      <div class="image">
        <nav>
        <router-link to="/index" active-class="active">主页</router-link>
        <router-link to="/news" active-class="active">新闻</router-link>
        <router-link to="/news" active-class="active">新闻</router-link>
        <router-link to="/news" active-class="active">新闻</router-link>
        <router-link to="/logon" active-class="active">登录</router-link>

        </nav>
      </div>
      <div class="login"> 
        <header>
          <h1>注册</h1>
          <el-divider>
            <i class="el-icon-s-check"></i>
          </el-divider>
          <div>
            已经有账号? <router-link to="/logon">点击登录</router-link>
            <!-- <router-link to="/logon">登录</router-link> -->
          </div>
        </header>
            <!-- 用户名解释 -->
        <el-popover
            ref="username"
            placement="right"
            title="用户名"
            width="150"
            trigger="focus"
            content="4-20个英文字母、数字以及下划线组合">
          </el-popover>
          <el-popover
            ref="password"
            placement="right"
            title="密码"
            width="150"
            trigger="focus"
            content="8-16个英文字母、数字组合,二者都要包含">
          </el-popover>
          
        <el-form :model="userInfo" status-icon :rules="rules" ref="userInfo" label-width="100px" class="demo-ruleForm">
          <el-form-item label="用户名" prop="username" class="input">
            <el-input type="text" v-model="userInfo.username" v-popover:username maxlength="20"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password" class="input">
            <el-input :type="passwordType1" v-model="userInfo.password" autocomplete="off" v-popover:password maxlength="16">
              <i slot="suffix" class="el-icon-view" id="i1" @click="showPass1"></i>
            </el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="checkPassword" class="input">
            <el-input :type="passwordType2" v-model="userInfo.checkPassword" autocomplete="off" maxlength="16"> 
              <i slot="suffix" class="el-icon-view" id="i2" @click="showPass2"></i>
            </el-input>
          </el-form-item>
          <el-form-item label="昵称" prop="nickname" class="input">
            <el-input type="text" v-model="userInfo.nickname"></el-input>
          </el-form-item>

          <el-form-item label="邮箱" prop="email" class="input">
            <el-input type="email" v-model="userInfo.email"></el-input>
          </el-form-item>

          <el-form-item>
            <div  class="button">
            <el-button type="success" @click="login('userInfo')" icon="el-icon-s-check">注册</el-button>
            <el-button type="info" @click="resetForm('userInfo')" icon="el-icon-s-release">重置</el-button>
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
  export default {
    name:'Login',
    data() {
      //校验用户名是否符合要求
      var validatorUsername = (rule, value, callback) => {
        if(!value){
          callback(new Error('请输入用户名'))
        }
        else{
          //校验用户名长度
          if(value.length >= 4 && value.length <= 20){
             //如果用户名中含有除了字母数字下划线以外的字符，则校验失败
            if(value.match(/\W+/g)){
            callback(new Error('用户名不符合要求,请重新输入'))
            }
            else{
              callback()
            }
          }
          else{
            //若长度不符合要求
            callback(new Error('用户名不符合要求,请重新输入'))
          }
          
        }
      }

      //校验密码
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.userInfo.checkPassword !== '') {
            this.$refs.userInfo.validateField('checkPassword');
          }
          if(!value.match(/^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]{8,16})$/g)){
            callback(new Error('密码不符合要求,请重新输入'))
          }
          else{
            callback();
          }
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.userInfo.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      //校验邮箱格式
      var validateEmail = (rule, value, callback) => {
        if(!value){
          callback('请输入邮箱')
        }
        else{
          if(value.match(/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$/g)){
          callback()
          }
          else{
            callback(new Error('邮箱格式错误'))
          }
        }
      }
      return {
        passwordType1:'password',
        passwordType2:'password',
        userInfo: {
          username: '',
          nickname: '',
          password: '',
          checkPassword: '',
          email: ''

        },
        rules: {
          username:[
            { validator: validatorUsername, required:true, trigger: 'blur'}
          ],
          password: [
            { validator: validatePass, required:true, trigger: 'blur' }
          ],
          checkPassword: [
            { validator: validatePass2, required:true, trigger: 'blur' }
          ],
          nickname:[
            {message: '请输入昵称', trigger: 'blur'}
          ],
          email:[
            {validator: validateEmail, required:true, trigger: 'blur'}
          ]
        }
      };
    },
    methods: {
      login(formName) {
        //校验表单是否符合规则
        this.$refs[formName].validate((valid) => {
          if (valid) {
            //发起axios请求，提交数据
            request('/user/login', 'POST', this.userInfo).then(
              response => {
                //请求成功回调
                this.$message({
                  message:'注册成功,3秒后自动跳转至登录界面',
                  type:'success'
                })             
                //跳转至登录界面
                setTimeout(() => {
                  this.$router.push('/logon')
                },3000)

              },
              error => {
                //请求失败回调
                if(error.data == 'existed'){
                  this.$message({
                  message:'用户名已注册',
                  type:'error'
                  })              
                }
                else{
                  console.log('错误类型',error.data);
                  this.$message({
                  message:'网络错误',
                  type:'error'
                  })          
                }
                //重新输入
                this.resetForm('userInfo')

              }

            )
          } else {
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      showPass1(){
        this.passwordType1 === 'password' ? this.passwordType1 = 'text' : this.passwordType1 = 'password';
        let e = document.getElementById('i1');
        this.passwordType1 == 'text' ? e.setAttribute('style', 'color: #409EFF') : e.setAttribute('style', 'color: #c0c4cc');
      },
      showPass2(){
        this.passwordType2 === 'password' ? this.passwordType2 = 'text' : this.passwordType2 = 'password';
        let e = document.getElementById('i2');
        this.passwordType2 == 'text' ? e.setAttribute('style', 'color: #409EFF') : e.setAttribute('style', 'color: #c0c4cc');
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
    background-image: url('../assets/img/login/1.1.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    height: 570px;
    width: 50%;
 
  }
  .login{
    display: flex;
    flex-direction: column;
    width: 440px;
    justify-content: center;
    padding: 60px;
    font-size: 14px;
    margin: 0px;

  }
  /* form{
    position: relative;
    left: 200px;
    top: 100px;
    height: 570px;
} */

  header{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  a{
    text-decoration: none;
    color: rgb(91, 145, 155);
  }
  a:hover{
    color: rgb(200, 255, 127);
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
/*
  .input{
    display: flex;
}
  */
</style>