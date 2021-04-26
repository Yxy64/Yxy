import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import list from './views/list.vue'
import message from './views/message.vue'
import maintain from './views/maintain.vue'
import logistics from './views/logistics.vue'
import hospitallist from './views/hospitallist.vue'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/About',
      name: 'About',
      component: About,
      children: [
        {
          path: '/list',
          name:'list',
          component: list
        },
        {
          path: '/message',
          name:'message',
          component: message
        },
        {
          path: '/maintain',
          name:'maintain',
          component: maintain
        },
        {
          path: '/logistics',
          name:'logistics',
          component: logistics
        },
        {
          path: '/hospitallist',
          name:'hospitallist',
          component: hospitallist
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