<template>
  <footer>

    <div class="footer-profile">
      <p class="profile">Profile</p>
      <img src="">
      <p class="name">Name</p>
      <p class="profile-text">ProfileText</p>
    </div>

    <div class="footer-top">
      <i class="fas fa-angle-double-up" @click="scrollToTop"></i>
    </div>

    <address>
      <ul>
        <li><a href="">Twitter</a></li>
        <li><a href="">GitHub</a></li>
        <li><a href="">Mail</a></li>
      </ul>
    </address>

    <small>copyright</small>
  </footer>
</template>

<script>
export default {
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      })
    }
  }
}
</script>

<style scoped>
footer {
  margin-top: 200px;
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
.footer-top {
  margin-bottom: 75px;
  text-align: center;
}
.footer-top i {
  font-size: 40px;
  width: 20px;
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
address ul li a {
  color: #000;
  text-decoration: none;
}
small {
  text-align: center;
  margin: 0 auto 50px;
  display: block;
}
@media (max-width: 480px) {
  .footer {
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
