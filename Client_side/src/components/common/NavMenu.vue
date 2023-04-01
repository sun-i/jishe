<template>
  <el-menu
    :default-active="'/paintLogin'"
    router
    mode="horizontal"
    background-color="white"
    text-color="#222"
    active-text-color="red"
    style="min-width: 1300px">
    <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
      {{ item.navItem }}
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: 'NavMenu',
  data () {
    return {
      navList: [
        {name: '/paintLogin', navItem: '病人登录'},
        {name: '/', navItem: '医生登录'}
      ]
    }
  }
}
</script>

<style scoped>

</style>

