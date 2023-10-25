<template>
  <footer>
    <div class="footer-profile">
      <p class="profile">Profile</p>
      <img src="" alt="Profile">
      <p class="name"></p>
      <p class="profile-text" :class="{ inactiveProfile: isEnglish }">自己紹介</p>
      <p class="profile-text" :class="{ inactiveProfile: !isEnglish }">Self Introduction</p>
    </div>

    <ul class="language">
      <li :class="{ active: isEnglish }" @click="translateIntoJapanese()">日本語</li>
      <li :class="{ active: !isEnglish }" @click="translateIntoEnglish()">English</li>
    </ul>

    <small>2023 xxx</small>
  </footer>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'footer',

  computed: {
    ...mapGetters([
      'currentPage',
    ]),
    isEnglish() {
      return this.$route.name === "postsEnglish" || this.$route.name === "detailEnglish"
    },
  },

  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      })
    },
    translateIntoJapanese() {
      if (this.$route.name === "postsEnglish") {
        this.$router.push({
          name: 'posts',
          query: {
            page: this.currentPage,
            tag: this.$route.query.tag
          }
        })
      }
      else if (this.$route.name === "detailEnglish") {
        this.$router.push({
          name: 'detail',
          params: { slug: this.$route.params.slug }
        })
      }
    },
    translateIntoEnglish() {
      if (this.$route.name === "posts") {
        this.$router.push({
          name: 'postsEnglish',
          query: {
            page: this.currentPage,
            tag: this.$route.query.tag
          }
        })
      }
      else if (this.$route.name === "detail") {
        this.$router.push({
          name: 'detailEnglish',
          params: { slug: this.$route.params.slug}
        })
      }
    }
  }
}
</script>

<style scoped>
footer {
  margin-top: 180px;
}
.footer-profile {
  background: #f2f2f2;
  width: 220px;
  margin: 0 auto 75px;
  padding: 30px;
  text-align: center;
}
.footer-profile img {
  width: 100px;
  margin: 30px;
}
.profile {
  width: 50px;
  margin: 0 auto;
}
.name {
  margin-bottom: 20px;
  font-weight: bold;
}
.profile-text {
  font-size: 12px;
  letter-spacing: 0.5px;
  line-height: 20px;
  text-align: left;
}
.inactiveProfile {
  display: none;
}
.footer-top {
  margin-bottom: 75px;
  text-align: center;
}
.footer-top img {
  width: 28px;
  cursor: pointer;
}
address {
  margin: 0 auto 80px;
}
address ul {
  width: 200px;
  margin: auto;
  list-style: none;
  display: flex;
  justify-content: space-around;
}
address ul li {
  display: inline-block;
}
address ul li img {
  height: 30px;
}
small {
  text-align: center;
  margin: 0 auto 50px;
  display: block;
}
.language {
  text-align: center;
  margin-bottom: 50px;
}
.language li {
  display: inline;
  margin-right: 1rem;
}
.active:hover{
  text-decoration: underline;
  cursor: pointer;
}

@media (max-width: 480px) {
  footer {
    margin-top: 70px;
  }
  .footer-profile {
    width: 80%;
    box-sizing: border-box;
  }
  .profile-text {
    font-size: 12px;
    line-height: 22px;
    letter-spacing: 0.5px;
  }
  .footer-top img {
    width: 30px;
  }
}
</style>
