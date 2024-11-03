<script>
export default {
  name: 'nearest-hidrant-content'
}
</script>

<template>
  <div class="nearest-content">
    <h1>Los hidrantes más cercanos a ti...</h1>
    <p>Dale click a una zona del mapa del Callao para determinar <br> tu ubicación y darte la ruta más corta para el hidrante de la capacidad deseada y más cercano a ti.</p>
    <div class="map-visualizer">
      <h1>MAP</h1>
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
  padding-top: 2rem;
}

</style>