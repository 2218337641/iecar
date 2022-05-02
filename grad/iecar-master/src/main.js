import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import axios from 'axios'
// import VueAxios from 'vue-axios'
import 'element-ui/lib/theme-chalk/index.css';

// 模拟数据
import '../mock/mock.js'

Vue.prototype.axios = axios
// Vue.prototype.qs = qs //使用方法为this.qs
Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
