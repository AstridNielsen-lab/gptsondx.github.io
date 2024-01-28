<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <RastreadorRuido />
  </div>
</template>

<script>
import RastreadorRuido from './components/RastreadorRuido.vue';

export default {
  name: 'App',
  components: {
    RastreadorRuido,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.logo {
  height: 300px;
}
</style>
