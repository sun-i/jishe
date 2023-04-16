import Vue from 'vue'
import Router from 'vue-router'
import AppIndex from '@/components/home/AppIndex'
import paintLogin from '@/components/PaintLogin'
import doctorLogin from '@/components/DoctorLogin'
import paintRegister from '@/components/PaintRegister'
import doctorRegister from '@/components/DoctorRegister'
import { name } from 'file-loader'

Vue.use(Router)



export default new Router({
  routes: [
    {
      path: '/paintLogin',
      name: 'paintLogin',
      component: paintLogin,
    },
    {
      path: '/',
      name: 'AppIndex',
      component: AppIndex,
    },
    {
      path: '/doctorLogin',
      name: 'doctorLogin',
      component: doctorLogin,
    },
    {
      path: '/paintRegister',
      name: 'paintRegister',
      component: paintRegister,
    },
    {
      path: '/doctorRegister',
      name: 'doctorRegister',
      component: doctorRegister,
    },
    {
      path: '/appointment',
      name: 'appointment',
      component: () => import('@/components/Appointment'),
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/patientIndex',
      name: 'patientIndex',
      component: () => import('@/components/PatientIndex'),
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/patientRecord',
      name: 'patientRecord',
      component: () => import('@/components/PatientRecord'),
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/doctorIndex',
      name: 'doctorIndex',
      component: () => import('@/components/DoctorIndex'),
      meta: {
        requireAuth: true
      }
    },
    {
      path:'/appointManage',
      name:'appointManage',
      component: () => import('@/components/AppointManage'),
      meta: {
        requireAuth: true
      }
    },
    {
      path:'/recordManage',
      name:'recordManage',
      component: () => import('@/components/RecordManage'),
      meta: {
        requireAuth: true
      }
    },
    {
      path:'/AIassistance',
      name:'AIassistance',
      component: () => import('@/components/AIassistance'),
      meta: {
        requireAuth: true
      }
    },
    {
      path:'/detail/:id',
      name:'detail',
      component: () => import('@/components/Detail'),
      meta: {
        requireAuth: true
      }
    },
    {
      path:'/medicRecord/:id',
      name:'medicRecord',
      component: () => import('@/components/MedicRecord'),
      meta: {
        requireAuth: true
      }
    },
    {
      path:'/uploadImg',
      name:'uploadImg',
      component: () => import('@/components/UploadImg'),
      meta: {
        requireAuth: true
      }
    },
    {
      path:'/report',
      name:'report',
      component: () => import('@/components/Report'),
      meta: {
        requireAuth: true
      }
    }
  ]
})


