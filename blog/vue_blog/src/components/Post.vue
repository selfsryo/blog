<template>

  <article class="container" v-if="post">

    <div class="post-header">
      <img class="post-thumbnail" :src="post.thumbnail"/>
      <div class="post-thumbnail-text" :style="{'color': post.color}" >
        <div class="post-created">{{(post.created_at)}}</div>
        <h2 class="post-title">{{post.title}}</h2>
        <ul class="post-tag">
          <li v-for="tag of post.tag" :key="tag.id" @click="updateSelectedTag(tag.id); search()"># {{tag.name}}</li>
        </ul>
      </div>
    </div>

    <div class="post-lead">{{post.lead_text}}</div>
    <p class="post-text" ref="postText" v-html="post.main_text"></p>

    <div class="navi">
      <transition-group tag="ul">
        <li v-show="isShowed" key="1" @click="showMaskedToc">
          <i class="fas fa-bars"></i>
        </li>
      </transition-group>
    </div>
    
    <div class="mask" ref="mask" @click="showMaskedToc"></div>
  </article>
  
</template>

<script>
import hljs from 'highlight.js'
import 'highlight.js/styles/night-owl.css'

export default {
  name: 'post',

  props: {
    slug: { type: String }
  },

  data() {
    return {
      post: null,
      selectedTag: this.$route.query.tag || '',
      isShowed: false
    }
  },

  mounted() {
    this.showNavi()

    this.$http(`${this.$httpPosts}${this.slug}/`)
      .then(response => {
        return response.json()
      })
      .then(data => {
        this.post = data
        document.title = `${data.title} - Blog`
        document.querySelector('meta[name="description"]').setAttribute('content', data.lead_text)
      })
  },

  updated() {
    this.setTocs()

    this.updateCodeSyntaxHighlighting()

    /* Mask a TOC when it is clicked */
    document.getElementById('maskedToc').addEventListener('click', this.showMaskedToc, false)
  },

  methods: {
    updateCodeSyntaxHighlighting() {
      // Apply highlight.js to <code> sections in <pre> sections
      document.querySelectorAll('pre code').forEach(block => {
        hljs.highlightBlock(block)
      })
    },

    updateSelectedTag(tag) {
      this.selectedTag = tag
    },

    search() {
      this.$router.push({
        name: 'posts',
        query: { page: 1, tag: this.selectedTag }
      })
    },

    showNavi() {
      window.addEventListener('scroll', () => {
        this.isShowed = window.scrollY > 1000 ? true : false
      })
    },

    showMaskedToc() {
      const maskedToc = document.getElementById('maskedToc')
      maskedToc.classList.toggle('show')
      this.$refs.mask.classList.toggle('show')
    },

    setTocs() {
      /* Operate a <div class='toc'> section included in HTML.
       * This function is hooked in updated after v-html work. */
      const toc = document.querySelector('.toc')
      toc.id = 'toc'

      // Insert '目次' at the beginning of TOC
      if (!document.getElementById('tocTitle')) {
        const tocTitle = document.createElement('p')
        tocTitle.id = 'tocTitle'
        tocTitle.textContent = '目次'
        toc.insertBefore(tocTitle, toc.firstChild)
      }
      
      // Create a masked TOC by cloning from the normally displayed TOC 
      if (!document.getElementById('maskedToc')) {
        const maskedToc = toc.cloneNode(true)
        this.$refs.postText.appendChild(maskedToc)
        maskedToc.id = 'maskedToc'
      }
    }
  },
}
</script>

<style scoped>
.container {
  margin: 100px auto 0;
  width: 1000px;
}
ul {
  list-style: none;
}
.post-header {
  margin: 50px auto;
  position: relative;
  text-align: center;
}
.post-thumbnail {
  width: 100%;
}
.post-thumbnail-text {
  margin: 0;
  padding: 0;
  width: 80%;
  text-align: center;
  transform: translate(-50%, -50%);
  position: absolute;
  top: 50%;
  left: 50%;
}
.post-created {
  font-size: 18px;
  font-weight: bold;
}
.post-title {
  font-size: 24px;
  margin: 20px auto;
}
.post-tag {
  margin-top: 20px;
  text-align: center;
}
.post-tag li {
  margin: auto 10px;
  font-size: 16px;
  display: inline;
  cursor: pointer;
}
.post-lead {
  margin: auto;
  padding: 60px 0;
  width: 80%;
  font-size: 14px;
  line-height: 26px;
  letter-spacing: 0.5px;
}
.post-text {
  margin: 0 auto;
  width: 80%;
}
.post-text :deep(h1), .post-text :deep(h2), .post-text :deep(h3), .post-text :deep(h4), .post-text :deep(h5) {
  text-align: center;
  margin: 40px auto 20px;
}
.post-text :deep(h1) {
  font-size: 18px;
  margin-top: 100px;
}
.post-text :deep(h2) {
  font-size: 17px;
  margin-top: 80px;
}
.post-text :deep(h3) {
  font-size: 16px;
}
.post-text :deep(h4) {
  font-size: 15px;
}
.post-text :deep(h5) {
  font-size: 14px;
}
.post-text :deep(p) {
  font-size: 14px;
  letter-spacing: 0.5px;
  line-height: 26px;
  margin-bottom: 16px;
}
.post-text :deep(blockquote) {
  border-left: 5px solid #ddd;
  color: #777;
  padding: 1em;
  padding-right: 0;
  margin: 1.5em 0;
}
.post-text :deep(blockquote) p {
  margin-bottom: 0;
}
.post-text :deep(ul){
  font-size: 14px;
}
.post-text :deep(table) {
  font-size: 14px;
  border-collapse: collapse;
  margin: 30px auto;
  text-align: center;
}
.post-text :deep(th) {
  background: #011627;
  color: #d6deeb;
  font-weight: normal;
}
.post-text :deep(th),
.post-text :deep(td) {
  padding: 5px;
  border: solid 1px;
}
.post-text :deep(a) {
  color: #000;
}
.post-text :deep(a):hover {
  color: #ff0000;
}
.post-text :deep(img) {
  width: 100%;
}
.post-text :deep(pre) {
  margin: 10px auto 30px;
  font-size: 14px;
}
.post-text :deep(.toc) {
  background: #f2f2f2;
  margin: 0 auto 100px;
  padding: 40px 80px;
}  
.post-text :deep(.toc a) {
  color: #123456;
  font-size: 16px;
  font-weight: bold;
  text-decoration: none;
}
.post-text :deep(.toc) ul ul a{
  color: #000;
  font-size: 14px;
  font-weight: normal;
}
.post-text :deep(.toc) p {
  font-size: 16px;
  font-weight: bold;
  text-align: center;
}
.post-text :deep(.toc) li {
  margin-top: 30px;
}
.post-text :deep(.toc) ul ul li {
  list-style: none;
  margin-top: 5px;
}
.mask,
.post-text :deep(#maskedToc) {
  opacity: 0;
  transition-property: opacity;
  transition-duration: 0.5s;
}
.post-text :deep(#maskedToc) {
  position: fixed;
  top: -999px;
}
.mask.show {
  background: rgba(0, 0, 0, 0.5);
  display: block;
  height: 100%;
  width: 100%;
  opacity: 1;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 2;
}
.post-text :deep(#maskedToc.show) {
  background: #fff;
  display: block;
  width: 60%;
  opacity: 1;
  transform: translate(-50%, -50%);
  position: fixed;
  top: 50%;
  left: 50%;
  z-index: 3;
}
.navi ul {
  display: flex;
  position: fixed;
  right: 5%;
  bottom: 60px;
}
.navi li {
  height: 50px;
  text-align: center;
  line-height: 50px;
  margin: auto 5px;
  border-radius: 100%;
  height: 50px;
  color: #666;
  background: rgba(255, 255, 255, 0.7);
  margin: auto 5px;
  cursor: pointer;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s;
}
.v-enter-from,
.v-leave-to {
  opacity: 0;
}
@media (max-width: 1024px) {
  .container {
    width: 100%;
  }
  .post-thumbnail {
    width: 90%;
  }
  .post-thumbnail-text {
    width: 70%;
  }
  .post-lead {
    width: 70%;
  }
  .post-text {
    width: 70%;
  }
}
@media (max-width: 768px) {
  .post-thumbnail {
    width: 100%;
  }
  .post-title {
    font-size: 22px;
  }
  .navi ul {
    right: 3%;
  }
}
@media (max-width: 480px) {
  .container {
    margin: 50px auto 0;
  }
  .post-header {
    margin: 0 auto 20px;
  }
  .post-title {
    font-size: 17px;
    line-height: 26px;
  }
  .post-created {
    font-size: 12.5px;
  }
  .post-lead {
    font-size: 13px;
    padding: 30px;
  }
  .post-tag li {
    font-size: 11px;
  }
  .post-lead, .post-text {
    width: 85%;
  }
  .post-text :deep(h1), .post-text :deep(h2), .post-text :deep(h3), .post-text :deep(h4), .post-text :deep(h5) {
    margin: 15px auto 10px;
  }
  .post-text :deep(h1) {
    font-size: 16px;
    margin-top: 35px;
  }
  .post-text :deep(h2) {
    font-size: 15px;
    margin-top: 25px;
  }
  .post-text :deep(h3) {
    font-size: 14px;
  }
  .post-text :deep(h4) {
    font-size: 13px;
  }
  .post-text :deep(h5) {
    font-size: 12px;
  }
  .post-text :deep(p) {
    font-size: 12.5px;
    letter-spacing: 0.3px;
    line-height: 22px;
  }
  .post-text :deep(.toc) {
    margin: 0 auto 50px;
    padding: 20px 50px;
  }
  .post-text :deep(.toc) li {
    margin-top: 20px;
  }
  .post-text :deep(.toc) a {
    font-size: 12.5px;
  }
  .post-text :deep(.toc) ul ul a{
    font-size: 11px;
  }
  .post-text :deep(.toc) p {
    font-size: 12.5px;
  }
  .navi ul {
    display: flex;
    right: 2%;
    bottom: 50px;
  }
  .navi li img {
    width: 50px;
  }
}
</style>
