<template>
    <div id="bgi">
      <div class="head">
          <div class="systemName">NAME</div>
          <el-row class="LRButton">
            <el-button type="primary" round @click="login()">登 录</el-button>
            <el-button type="primary" round @click="register()">注 册</el-button>
          </el-row>
          <div class="s-link">
            <el-link ref="/">主页</el-link>
            <el-link>关于</el-link>
            <el-link icon="iconfont icon-QQ-copy"></el-link>
            <el-link icon="iconfont icon-weixin"></el-link>
            <el-link icon="iconfont icon-dingding"></el-link>
          </div>
      </div>
      <h1>一键式肿瘤智能检测平台</h1>
      <h3>ababaabbabbababbadbsadbska</h3>
      <div class="startButton">
        <el-button type="primary">了解更多</el-button>
        <el-button type="primary" plain @click="login()">立即体验</el-button>
      </div>
      <div class="bottom">
        <div class="bottomLink">
          <el-link>关于我们</el-link>
          <el-link>联系我们</el-link>
          <el-link>使用条款</el-link>
          <el-link>隐私政策</el-link>
        </div>
        <div class="bottomInfo">
          <p>© Design by SX ZY</p>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    name: 'AppIndex',
    methods: {
      login() {
        this.$router.push('/PaintLogin')
      },
      register() {
        this.$router.push('/PaintRegister')
      }
    }

  }
</script>

<style scoped>
  .head {
    height: 60px;
    width: 100%;
  }
  .systemName {
    margin: 20px 50px;
    float: left;
    font-size: 20px;
    font-weight: bold;
    color: #f4f2f3;
  }
  .s-link {
    margin: 20px 30px;
    margin-right: 0;
    float: right;
  }
  .s-link .el-link:hover {
    color: #409EFF;
  }
  .s-link .el-link {
    margin: 0px 15px;
    font-size: 18px;
    font-weight: bold;
    color: aliceblue;
  }

  .s-link >>> .iconfont {
    font-size: 22px;
    color: aliceblue;
  }
  .s-link >>> .iconfont:hover {
    color: #409EFF;
  }

  .LRButton {
    margin: 15px 30px 0 0;
    float: right;
  }
  .LRButton .el-button {
    padding: 0;
    width: 80px;
    line-height: 35px;
    height: 35px;
    margin: 0px 10px;
    font-size: 14.5px;
  }

  h1 {
    margin-top: 130px;
    color:aliceblue;
    font-weight: 550;
  }
  h3 {
    color:aliceblue;
  }

  .startButton {
    margin-top: 50px;
  }
  .startButton .el-button {
    padding: 0;
    width: 170px;
    line-height: 50px;
    height: 50px;
    margin: 0px 40px;
    font-size: 18px;
    font-weight: 400;
  }

  #bgi {
    width: 100%;
    height: 100%;
    background-image: url("../../assets/home_bg.jpg");
    background-position: center;
    background-size: cover;
    position: fixed;
  }

  .bottom {
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 60px;
    color: aliceblue;
  }

  .bottomLink .el-link{
    margin: 20px 30px;
    margin-right: 0;
    float: left;
    color: aliceblue;
  }

  .bottomInfo {
    margin: 20px 30px;
    margin-right: 50px;
    float: right;
    color: aliceblue;
  }

</style>

