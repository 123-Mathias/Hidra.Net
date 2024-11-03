<script>
export default {
  name: 'hidrants-net-content'
}
</script>

<template>
  <div class="hidrants-net-content">
    <h1>Red de Hidrantes del Callao</h1>
    <p>Visualiza la Red óptima de hidrantes para su correcto mantenimiento. Con esta red <br> se tendrá un mantenimiento mucho más eficiente y exitoso de los hidrantes de la ciudad del Callao.</p>
    <div class="map-visualizer">
      <h1>MAP</h1>
    </div>
  </div>
</template>

<style scoped>

.hidrants-net-content{
  padding: 5rem 2rem;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
}

.hidrants-net-content h1,p{
  color: #4E171C;
  text-align: center;
}

.hidrants-net-content p{
  padding-top: 1.5rem;
}


.map-visualizer{
  padding-top: 2rem;
}

</style>