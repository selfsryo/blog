import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

Vue.prototype.$http = (url, opts) => fetch(url, opts)
Vue.prototype.$httpPosts = 'http://127.0.0.1:8000/api/posts/'
Vue.prototype.$httpTags = 'http://127.0.0.1:8000/api/tags/'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
