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

/* Loading animation https://tobiasahlin.com/spinkit/ */
.spinner {
  background-color: #333;
  width: 50px;
  height: 50px;
  position: fixed;
  top: 400px;
  left:calc(50% - 50px/2);
  z-index: 3;
  border-radius: 100%;
  -webkit-animation: sk-scaleout 1.0s infinite ease-in-out;
  animation: sk-scaleout 1.0s infinite ease-in-out;
}
@-webkit-keyframes sk-scaleout {
  0% { -webkit-transform: scale(0) }
  100% {
    -webkit-transform: scale(1.0);
    opacity: 0;
  }
}
@keyframes sk-scaleout {
  0% {
    -webkit-transform: scale(0);
    transform: scale(0);
  } 100% {
    -webkit-transform: scale(1.0);
    transform: scale(1.0);
    opacity: 0;
  }
}
@media (max-width: 1024px) {
  .spinner {
    width: 40px;
    height: 40px;
    left:calc(50% - 40px/2);
  }
}
@media (max-width: 480px) {
  .spinner {
    width: 30px;
    height: 30px;
    top: 320px;
    left:calc(50% - 30px/2);
  }
}

</style>
