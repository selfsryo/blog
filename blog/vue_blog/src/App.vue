<template>
  <div id="nav">
    <Header />
    <div class="router">
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header';
import Footer from './components/Footer';
export default {
  name: "app",
  components: { Header, Footer }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  font-family: 'Karla', 'Hiragino Kaku Gothic Pro', sans-serif;
}
body {
  margin: auto;
}
.router {
  min-height: 100vh;
}
</style>
