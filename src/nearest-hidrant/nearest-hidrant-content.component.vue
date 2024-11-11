<script>

export default {
  name: 'nearest-hidrant-content',
  data() {
    return {
      mapUrl: "",
    }
  },
  mounted() {
    this.fetchMap();
  },
  methods: {
    fetchMap() {
      this.mapUrl = `http://127.0.0.1:5000/api/v1.0/nearHydrants_map?timestamp=${new Date().getTime()}`
    },
  }
}
</script>

<template>
  <div class="nearest-content">
    <h1>Los hidrantes más cercanos a ti...</h1>
    <p>Dale click a una zona del mapa del Callao para determinar <br> tu ubicación y darte la ruta más corta para el hidrante de la capacidad deseada y más cercano a ti.</p>
    <div class="map-visualizer">
      <h1>MAP</h1>
      <iframe class="map" v-if="mapUrl" :src="mapUrl" width="90%" allowfullscreen height="500px" style="border: 3px solid #4E171C;"></iframe>
      <button v-if="mapUrl" class="button-calculate" @click="fetchMap">Calcular Ruta</button>
      <div class="loading" v-if="!mapUrl">
        <div class="spinner"></div>
        <p>Cargando mapa...</p>
      </div>
    </div>
  </div>

</template>

<style scoped>

.nearest-content{
  padding: 5rem 2rem;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
}

.nearest-content h1,p{
  color: #4E171C;
  text-align: center;
}

.nearest-content p{
  padding-top: 1.3rem;
}

.map-visualizer{
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 2rem;
}

.button-calculate{
  background-color: #4E171C;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 1rem;
  font-size: 1.5rem;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 500px;
  width: 90%;
  border: 3px solid #4e171c;
  border-radius: 5px;
  color: #4e171c;
  font-size: 1.2rem;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #4e171c;
  border-top: 5px solid transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

</style>