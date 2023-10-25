import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'


const app = createApp(App).use(store).use(router)

app.config.globalProperties.$http = (url, opts) => fetch(url, opts)
app.config.globalProperties.$httpPosts = process.env.VUE_APP_API_POSTS
app.config.globalProperties.$httpEnglishPosts = process.env.VUE_APP_API_EN_POSTS
app.config.globalProperties.$httpTags = process.env.VUE_APP_API_TAGS

app.mount('#app')
