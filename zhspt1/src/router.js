import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import bclass from './views/bclass.vue'
import bdormitory from './views/bdormitory.vue'
import bstudent from './views/bstudent.vue'
import index from './views/index.vue'
import sdhygiene from './views/sdhygiene.vue'
import sddevice from './views/sddevice.vue'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/About',
      name: 'About',
      component: About,
      redirect: '/index',
      children: [
        {
          path: '/bclass',
          name: 'bclass',
          component: bclass
        },
        {
          path: '/bdormitory',
          name: 'bdormitory',
          component: bdormitory
        },
        {
          path: '/bstudent',
          name: 'bstudent',
          component: bstudent
        },
        {
          path: '/index',
          name: 'index',
          component: index
        },
        {
          path: '/sdhygiene',
          name: 'sdhygiene',
          component: sdhygiene
        },
        {
          path: '/sddevice',
          name: 'sddevice',
          component: sddevice
        }
      ]
    },
  ]
});

router.beforeEach((to, from, next) => {
  if (to.path === '/') return next()

  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/')
  next()
});

export default router;
