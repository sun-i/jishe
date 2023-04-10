<template>
  <div class="bg">
    <el-form class="login-container" label-position="left"
             label-width="0px">
      
    <el-menu :default-active="'/doctorLogin'" router class="el-menu-demo" mode="horizontal">
      <el-menu-item index="/paintLogin">病人登录</el-menu-item>
      <el-menu-item index="/doctorLogin">医生登录</el-menu-item>
    </el-menu>
      
      
      <el-form-item>
        <el-input type="text" v-model="loginForm.username"
                  auto-complete="off" placeholder="账号"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input type="password" v-model="loginForm.password"
                  auto-complete="off" placeholder="密码"></el-input>
                  <el-link href="#" class="wangji">忘记密码</el-link>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button type="primary" style="width: 100%;background: #505458;border: none" v-on:click="login">登录</el-button>
      </el-form-item>
      <div>
        <el-link type="primary" href="#/doctorRegister">没有账号？去注册</el-link>
      </div>
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
          .post('user/doctor/login/', this.$qs.stringify({
            username: this.loginForm.username,
            password: this.loginForm.password
          }), {// 发送表单格式数据
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          })
          .then(successResponse => {
            console.log("success")
            console.log(successResponse)
            if (successResponse.data.code === 200) {
                this.$store.commit('login', successResponse.data)
                this.$message({
                    message: '登录成功',
                    type: 'success'
                  });
                this.$router.push({path: '/patientIndex'})
            }
            else {
                this.$message.error(successResponse.data.msg)
            }
          })
          .catch(failResponse => {
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

  .wangji {
    margin-top: 5px;
    float: right;
    font-size: 10px;
    height: 20px;
    line-height: 20px;
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
