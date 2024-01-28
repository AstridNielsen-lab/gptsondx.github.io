<!-- Instale o Vue.js com: npm install -g vue -->
<template>
  <div>
    <button @click="escanear">Escanear Frequências</button>
    <div v-for="frequencia in frequencias" :key="frequencia">
      {{ frequencia }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      frequencias: []
    };
  },
  methods: {
    escanear() {
      // Coloque aqui a lógica para chamar a API Flask e atualizar as frequências
      this.frequencias = ["2.5 GHz", "850 MHz - 2100 MHz"];
    }
  }
};
</script>
