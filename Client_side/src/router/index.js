import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AppIndex from '@/components/home/AppIndex'
import Login from '@/components/Login'

Vue.use(Router)



export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login,
      redirect: '/paintLogin',
      children: [
        {
          path: '/paintLogin',
          name: 'PaintLogin',
          component: () => import('@/components/PaintLogin')
        }
      ]

    },
    {
      path: '/index',
      name: 'AppIndex',
      component: AppIndex,
      meta: {
        requireAuth: true
      }
    },
  ]
})


