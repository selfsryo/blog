<template>
  <section class="container">

    <router-link class="blog-logo" :class="{ inactive: isEnglish }" :to="{name: 'posts'}">
      <img src="">
    </router-link>
    <router-link class="blog-logo blog-logo-en" :class="{ inactive: !isEnglish }" :to="{name: 'postsEnglish'}">
      <img class="logo" src="">
    </router-link>

    <ul class="tag-filter">
      <li class="category">CATEGORY</li>
      <li>
        <select v-model="selectedTag" @change="search()">
          <option value="" :key="-1">all</option>
          <option v-for="tag of tagList" :value="tag.id" :key="tag.id">{{tag.name}}</option>
        </select>
      </li>
    </ul>

    <div v-if="!loaded">
      <div class="spinner"></div>
      <div class="loadingMask"></div>
    </div>

    <article class="post" v-for="post of postList" :key="post.slug">
      <router-link class="post-title" :class="{ inactive: isEnglish }" :to="{name: 'detail', params: {slug: post.slug}}">{{post.title}}</router-link>
      <router-link class="post-title" :class="{ inactive: !isEnglish }" :to="{name: 'detailEnglish', params: {slug: post.slug}}">{{post.title}}</router-link>
      <div class="post-date">{{(post.created_at)}}</div>
      <img class="post-thumbnail" :src="post.thumbnail"/>
      <p class="post-lead">{{post.lead_text}}</p>
      <div class="post-more">
        <router-link :class="{ inactive: isEnglish }" :to="{name: 'detail', params: {slug: post.slug}}"><span class="right">▶︎ </span><span class="more">more</span></router-link>
        <router-link :class="{ inactive: !isEnglish }" :to="{name: 'detailEnglish', params: {slug: post.slug}}"><span class="right">▶︎ </span><span class="more">more</span></router-link>
      </div>
      <ul class="post-tag">
        <li :style="{'background': tag.color}" v-for="tag of post.tag" :key="tag.id" @click="updateSelectedTag(tag.id); search()"> # {{tag.name}}</li>
      </ul>
    </article>

    <div class="page-link" v-if="totalPages >= 2">
      <router-link class="previousPage" id="back" v-if="previousPageURL" :to="getPageURL(currentPage - 1)">＜</router-link>
      <div class="page-number">
        <router-link :class="{'currentPage': page === currentPage}" v-for="page of totalPages" :key="page" :to="getPageURL(page)">
          {{page}}
        </router-link>
      </div>
      <router-link class="nextPage" id="next" v-if="nextPageURL" :to="getPageURL(currentPage + 1)">＞</router-link>
    </div>

  </section>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { UPDATE_TAGS, UPDATE_POSTS } from '../store/mutation-types'
export default {
  name: 'post-list',

  data() {
    return {
      selectedTag: this.$route.query.tag || '',
      loaded: false
    }
  },

  watch: {
    $route() {
      this.loaded = false
      this.getPosts()
      this.selectedTag = this.$route.query.tag || ''
    },
  },

  created() {
    this.getPosts()

    this.$http(this.$httpTags)
      .then(response => {
        return response.json()
      })
      .then(data => {
        this[UPDATE_TAGS](data)
      })
  },

  mounted() {
    if (!this.isEnglish) {
      document.title = `記事一覧 - Blog`
      document.querySelector('meta[name="description"]').setAttribute("content", "ブログです。")
      document.querySelector('meta[property="og:description"]').setAttribute("content", "ブログです。")
    }
    else {
      document.title = `List of Articles - Blog`
      document.querySelector('meta[name="description"]').setAttribute("content", "Blog")
      document.querySelector('meta[property="og:title"]').setAttribute("content", "Blog")
      document.querySelector('meta[property="og:description"]').setAttribute("content", "Blog")
    }
  },

  computed: {
    ...mapGetters([
      'postList',
      'tagList',
      'currentPage',
      'totalPages',
      'previousPageURL',
      'nextPageURL',
    ]),
    isEnglish() {
      return this.$route.name === 'postsEnglish'
    },
  },

  methods: {
    ...mapActions([UPDATE_TAGS, UPDATE_POSTS]),

    getPosts() {
      let postURLs = this.isEnglish ? this.$httpEnglishPosts : this.$httpPosts
      if (location.search) {
        postURLs += location.search
      }
      this.$http(postURLs)
        .then(response => {
            return response.json()
        })
        .then(data => {
          this[UPDATE_POSTS](data)
          this.loaded = true
        })
    },

    getPageURL(page) {
      return this.$router.resolve({
        name: this.$route.name,
        query: {page, tag: this.selectedTag }
      }).fullPath
    },

    updateSelectedTag(tag) {
      this.selectedTag = tag
    },

    search() {
      this.$router.push({
        name: this.$route.name,
        query: { page: 1, tag: this.selectedTag }
      })
    },
  }
};
</script>

<style scoped>
.container {
  width: 800px;
  margin: auto;
}
ul {
  list-style: none;
}
.inactive {
  display: none !important;
}
.blog-logo {
  display: block;
  width: 400px;
  margin: 90px auto 80px;
  text-align: center;
  cursor: pointer;
}
img.logo {
  width: 100%
}
.blog-logo-en {
  margin-bottom: 60px !important;
}
.tag-filter {
  border-bottom: #ddd solid 1px;
  font-size: 14px;
  padding-bottom: 20px;
  text-align: right;
}
.tag-filter li{
  display: inline;
  margin-left: 10px;
}
.tag-filter select {
  background: #eee;
  border: none;
  border-radius: 3px;
  padding: 3px;
  text-align: center;
  outline: none;
}
article {
  border-bottom: #ddd solid 1px;
  padding: 70px 0;
}
.post-title {
  color: #000;
  display: inline-block;
  font-size: 20px;
  font-weight: bold;
  letter-spacing: 0.5px;
  margin-bottom: 10px;
  text-decoration: none;
  cursor: pointer;
}
.post-title:hover {
  text-decoration: underline;
}
.post-date {
  color: #aaa;
  font-size: 15px;
  font-weight: normal;
  margin-bottom: 30px;
}
.post-thumbnail {
  height: 246px;
  width: 368px;
  margin-bottom: 25px;
}
.post-lead {
  font-size: 14px;
  letter-spacing: 0.5px;
}
.post-more {
  text-align: right;
  margin: 10px auto;
}
.post-more a {
  color: #aaa;
  text-decoration: none;
}
.post-more span.right{
  font-size: 1px;
}
.post-more span.more{
  font-size: 14px;
  border-bottom: #aaa 1px solid;
  letter-spacing: 1px;
}
.post-tag {
  width: 100%;
}
.post-tag li {
  float: left;
  font-size: 14px;
  padding: 3px 10px 3px 5px;
  margin-right: 20px;
  margin-bottom: 10px;
  cursor: pointer;
  display: block;
}
.page-link {
  display: flex;
  margin: 70px auto 0;
  font-size: 15px;
  position: relative;
}
.page-link a {
  color: #bbb;
  text-decoration: none;
}
.page-number {
  display: flex;
  margin: auto;
  width: 150px;
  justify-content: space-between;
}
.page-number .currentPage, .page-link .previousPage, .page-link .nextPage {
  color: #000;
}
.page-link .previousPage, .page-link .nextPage {
  font-size: 12px;
  position: absolute;
}
.page-number .currentPage {
  text-decoration: underline;
}
.page-link .previousPage {
  left: 30%;
}
.page-link .nextPage {
  right: 30%;
}
.loadingMask {
  background: #fff;
  display: block;
  height: 8000px;
  width: 100%;
  position: absolute;
  top: 350px;
  left: 0;
  z-index: 2;
}
@media (max-width: 1024px) {
  .container {
    width: 70%;
  }
}
@media (max-width: 768px) {
  .tag-filter select {
    font-size: 16px;
    transform: scale(0.8);
  }
}
@media (max-width: 480px) {
  .container {
    width: 85%;
  }
  .blog-logo {
    width: 90%;
    margin-bottom: 40px !important;
  }
  .tag-filter li{
    margin-left: 6px;
  }
  .tag-filter li.category{
    font-size: 11px;
  }
  article {
    padding: 40px 0 70px;
  }
  .post-title {
    font-size: 15px;
  }
  .post-date {
    font-size: 11px;
  }
  .post-thumbnail {
    width: 100%;
    height: initial;
  }
  .post-lead {
    font-size: 12px;
  }
  .page-number {
    width: 110px;
  }
  .page-link .previousPage {
    left: 15%;
  }
  .page-link .nextPage {
    right: 15%;
  }
  .loadingMask {
    top: 300px;
  }
}
</style>
