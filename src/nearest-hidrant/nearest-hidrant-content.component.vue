<script>
import axios from "axios";

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
      this.mapUrl='http://127.0.0.1:5000/api/v1.0/nearHydrants_map'
    }
  }
}
</script>

<template>
  <div class="nearest-content">
    <h1>Los hidrantes más cercanos a ti...</h1>
    <p>Dale click a una zona del mapa del Callao para determinar <br> tu ubicación y darte la ruta más corta para el hidrante de la capacidad deseada y más cercano a ti.</p>
    <div class="map-visualizer">
      <h1>MAP</h1>
      <iframe v-if="mapUrl" :src="mapUrl" width="90%" allowfullscreen height="500px" style="border:none;"></iframe>
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
  padding-top: 1.5rem;
}

.map-visualizer{
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 2rem;
}

</style>