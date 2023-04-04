<template>
    <div class="bg">
      <el-form class="login-container" label-position="left"
             label-width="0px">
      
    <el-menu :default-active="'/paintRegister'" router class="el-menu-demo" mode="horizontal">
      <el-menu-item index="/paintRegister">病人注册</el-menu-item>
      <el-menu-item index="/doctorRegister">医生注册</el-menu-item>
    </el-menu>
      
      <el-form-item>
        <el-input type="text" v-model="loginForm.username"
                  auto-complete="off" placeholder="账号"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input type="password" v-model="loginForm.password"
                  auto-complete="off" placeholder="密码"></el-input>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button type="primary" style="width: 100%;background: #505458;border: none" v-on:click="login()">注册</el-button>
      </el-form-item>
    </el-form>
    </div>
  </template>
<script>

  export default {
    name: 'Login',
    data () {
      return {
        loginForm: {
          username: '',
          password: ''
        },
        responseResult: [],
      }
    },
    methods: {
      login () {
        this.$axios 
          .post('user/patient/register/', this.$qs.stringify({
            username: this.loginForm.username,
            password: this.loginForm.password
          }), {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          })
          .then(successResponse => {
            if (successResponse.data.code === 200) {
                this.$router.push({path: '/paintLogin'})
            }
          })
          .catch(failResponse => {
            this.$message.error("Error")
          })
      }
    }
  }
</script>

<style scoped>
  .el-menu-item {
    margin: 0 0 50px 0;
    width: 50%;
  }

  .el-menu.el-menu--horizontal {
    border-bottom: none;
  }

  .login-container {
    border-radius: 15px;
    /* background-clip: padding-box; */
    margin: 120px auto;
    width: 350px;
    padding: 20px 40px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }
  
  .login_title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
  }

  .bg {
    width: 100%;
    height: 100%;
    background-image: url("../assets/home_bg.jpg") ;
    background-position: center;
    background-size: cover;
    position: fixed;
  }
</style>
