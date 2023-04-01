<template>
    <div>
      <NavMenu/>
      <router-view/>
    </div>
  </template>
  
  <script>
    import NavMenu from '@/components/common/NavMenu'
    export default {
      name: 'Login',
      components: {
        NavMenu
      }
    }
  </script>
  
  <style scoped>
  
  </style>
  