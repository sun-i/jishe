import Vue from 'vue'
import Router from 'vue-router'
import AppIndex from '@/components/home/AppIndex'
import paintLogin from '@/components/PaintLogin'
import doctorLogin from '@/components/DoctorLogin'
import paintRegister from '@/components/PaintRegister'
import doctorRegister from '@/components/DoctorRegister'

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
    },
    {
      path: '/patientIndex',
      name: 'patientIndex',
      component: () => import('@/components/PatientIndex'),
    },
    {
      path: '/patientRecord',
      name: 'patientRecord',
      component: () => import('@/components/PatientRecord'),
    }
  ]
})


