<template>
  <header>
    <div class="header">

      <router-link :to="{name: 'posts'}">
        <p class="header-logo">blog</p>
      </router-link>

      <ul class="header-link">
        <li><a href="">Twitter</a></li>
        <li><a href="">GitHub</a></li>
        <li><a href="">Mail</a></li>
      </ul>

    </div>
  </header>
</template>

<style scoped>
.header {
  width: 900px;
  margin: 0 auto 20px;
}
.header-logo {
  color: #000;
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
@media (max-width: 1024px) {
  .header {
    width: 70%;
  }
}
@media (max-width: 480px) {
  .header-link {
    top: 15px;
    right: 13px;
    line-height: 7px;
  }
  .header-link a {
    margin: 0 0 0 15px;
  }
}
</style>
