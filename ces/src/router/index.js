import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import zy from '../App.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'zy',
    component: zy
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/home',
    name: 'home',
    component:HomeView
  }
]

const router = new VueRouter({
  routes
})

export default router
