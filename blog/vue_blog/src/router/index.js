import { createRouter, createWebHistory } from 'vue-router'
import PostList from '@/components/PostList'
import Post from '@/components/Post'


const routes = [
  {
    path: '/',
    name: 'posts',
    component: PostList
  },
  {
    path: '/detail/:slug',
    name: 'detail',
    component: Post,
    props: routes => ({
      slug: routes.params.slug,
    })
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { left: 0, top: 0 }
    }
  }
})

export default router
