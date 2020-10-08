import { createStore } from 'vuex'
import { UPDATE_POSTS, UPDATE_TAGS } from './mutation-types'


export default createStore({
  strict: process.env.NODE_ENV !== 'production',

  state: {
    posts: {},
    tags: [],
  },

  getters: {
    postList(state) {
      return state.posts.results
    },
    tagList(state) {
      return state.tags
    },
    currentPage(state) {
      return state.posts.current_page
    },
    totalPages(state) {
      return state.posts.total_pages
    },
    previousPageURL(state) {
      return state.posts.previous
    },
    nextPageURL(state) {
      return state.posts.next
    },
  },

  mutations: {
    [UPDATE_POSTS](state, payload) {
      state.posts = payload
    },
    [UPDATE_TAGS](state, payload) {
      state.tags = payload
    },
  },

  actions: {
    [UPDATE_POSTS]({ commit }, payload) {
      commit(UPDATE_POSTS, payload)
    },
    [UPDATE_TAGS]({ commit }, payload) {
      commit(UPDATE_TAGS, payload)
    }
  },

  modules: {}
})
