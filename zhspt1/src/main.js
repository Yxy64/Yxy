import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '@/assets/fonts/iconfont.css'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';

Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.use(ElementUI);
Vue.use(ViewUI);

// axios.interceptors.request.use(config => {
//   console.log(config);
//   config.headers.Authorization = window.sessionStorage.getItem('token')
//   return config;
// })

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
