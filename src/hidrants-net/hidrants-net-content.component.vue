<script>
import axios from 'axios';

export default {
  name: 'hidrants-net-content',
  data() {
    return {
      map_url: "",
      total_cost: null
    }
  },
  mounted() {
    this.fetchMap(); // Cargar el mapa automáticamente al montar el componente
  },
  methods: {
    fetchMap() {
      axios.get('http://127.0.0.1:5000/api/v1.0/hydrants_map')
          .then(response => {
            this.map_url = response.data.map_url;
            this.total_cost = response.data.total_cost;
          }).catch((error) => {
            console.log(error)
          })

    }
  }
}
</script>

<template>
  <div class="hidrants-net-content">
    <h1>Red de Hidrantes del Callao</h1>
    <p>Visualiza la Red óptima de hidrantes para su correcto mantenimiento. Con esta red <br> se tendrá un mantenimiento mucho más eficiente y exitoso de los hidrantes de la ciudad del Callao.</p>
    <div class="map-visualizer">
      <h1 class="title_map">MAP</h1>
      <iframe v-if="map_url" :src="map_url" width="90%" allowfullscreen height="500px" style="border:none;"></iframe>
      <h1 class="total_cost">El costo total de los caminos en km es: {{total_cost}} </h1>
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
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 2rem;
}

</style>