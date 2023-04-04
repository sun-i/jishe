<template>
    <el-container>
        <el-header>
            <h3>NAME 检测</h3>
            <el-input placeholder="请输入内容" class="input-with-select">
                <el-button slot="append" icon="el-icon-search"></el-button>
            </el-input>
        </el-header>
        <el-aside width="200px">Aside</el-aside>
        <el-main>Main</el-main>
    </el-container>
</template>
  
<style scoped>
    h3 {
        margin: 20px 50px;
        float: left;
    }

    .input-with-select {
        float: left;
        width: 300px;
        margin: 20px 50px;
        border-radius: 50px;
    }

    
</style>
  
<script>
    export default {
      name: 'Appointment',
    };
</script>