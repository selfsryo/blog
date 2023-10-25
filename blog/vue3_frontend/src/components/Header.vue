<template>
  <header>
    <div class="header">

      <router-link :class="{ inactive: isEnglish }" :to="{name: 'posts'}">
        <p class="header-logo"><img src="" alt="header"> </p>
      </router-link>
      <router-link :class="{ inactive: !isEnglish }" :to="{name: 'postsEnglish'}">
        <p class="header-logo"><img src="" alt="header"> </p>
      </router-link>

      <ul class="header-link">
        <li><a href="" target="_blank" rel="noreferrer"><img src="" alt="Twitter"></a></li>
        <li><a href="" target="_blank" rel="noreferrer"><img src="" alt="GitHub"></a></li>
        <li><a href="" target="_blank" rel="noreferrer"><img src="" alt="Mail"></a></li>
      </ul>

    </div>
  </header>
</template>

<script>
export default {
  name: 'header',

  computed: {
    isEnglish() {
      return this.$route.name === "postsEnglish" || this.$route.name === "detailEnglish"
    },
  }
}
</script>

<style scoped>
.header {
  width: 900px;
  margin: 0 auto 20px;
}
.inactive {
  display: none;
}
.header-logo img{
  width: 120px;
  position: absolute;
  top: 30px;
  left: 30px;
}
.header-link {
  display: flex;
  list-style: none;
  position: absolute;
  top: 30px;
  right: 30px;
}
.header-link a {
  color: #000;
  font-size: 16px;
  font-weight: bold;
  margin-left: 10px;
  text-decoration: none;
}
.header-link img {
  height: 20px;
}
@media (max-width: 1024px) {
  .header {
    width: 70%;
  }
}
@media (max-width: 480px) {
  .header-logo img{
    width: 90px;
  }
  .header-link {
    top: 15px;
    right: 13px;
    line-height: 7px;
  }
  .header-link a {
    margin: 0 0 0 15px;
  }
  .header-link img {
    height: 17px;
  }
  .header-logo img {
    top: 16px;
    left: 13px;
  }
}
</style>
