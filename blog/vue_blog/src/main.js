import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'


const app = createApp(App).use(store).use(router)

app.config.globalProperties.$http = (url, opts) => fetch(url, opts)
app.config.globalProperties.$httpPosts = 'http://127.0.0.1:8000/api/posts/'
app.config.globalProperties.$httpTags = 'http://127.0.0.1:8000/api/tags/'

app.mount('#app')
