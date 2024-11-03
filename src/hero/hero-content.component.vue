<script>
export default {
  name: 'hero-content'
}
</script>

<template>
  <div class="hero-content">
    <div class="hero-main">
      <div class="hero-title">
        <p>Con Hidra.Net</p>
        <h1>Sé parte de la solución, encuentra el hidrante más cercano a ti.</h1>
        <p class="phrase">En cada hidrante, encontramos un símbolo de esperanza y protección, un faro de seguridad en momentos de crisis. - Jorge Valdivia.</p>
        <div class="check-benefits">
          <img src="/public/hero-images/check-icon.png" class="check-image" alt="Check icon">
          <p>Fácil de usar</p>
        </div>
        <div class="check-benefits">
          <img src="/public/hero-images/check-icon.png" class="check-image" alt="Check icon">
          <p>Diseño intuitivo</p>
        </div>
        <div class="check-benefits">
          <img src="/public/hero-images/check-icon.png" class="check-image" alt="Check icon">
          <p>Abastecimiento de todo el Callao</p>
        </div>
      </div>
      <div class="hero-image-main">
        <img src="/public/hero-images/hidrants-image.jpg" class="image" alt="hidrants image">
      </div>
    </div>
    <div class="hero-final">
      <div class="hero-image-final">
        <img src="/public/hero-images/callao-map.jpg" class="callao-map" alt="Callao Map">
      </div>
      <div class="hero-final-text">
        <h1 class="darkred-1">¡Visualiza todos los hidrantes <br> del Callao!</h1>
        <p class="darkred-2">Próximamente podrás visualizar los hidrantes de toda <br> <span class="italic"> Lima Metropolitana.</span></p>
      </div>
    </div>
  </div>
</template>

<style scoped>

.italic{
  font-style: italic;
  color: #9e313b;
}

.check-image{
  width: 30px;
  height: 30px;
}

.check-benefits {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding-top: 1rem;
}

.check-benefits p{
  padding-top: 0.25rem;
}

.hero-main{
  display: flex;
  padding-top: 2rem;
}

.hero-title {
  padding: 4rem 3rem; /* Asegúrate de que el padding esté establecido */
  width: 50%;
  background-color: #4E171C;
  box-sizing: border-box; /* Incluye el padding en el cálculo del ancho */
}

.hero-title h1{
  overflow-wrap: break-word; /* Permite que las palabras se dividan si son demasiado largas */
  word-wrap: break-word; /* Para compatibilidad con navegadores antiguos */
  width: 100%; /* Asegúrate de que el ancho sea 100% del contenedor */
  margin: 0; /* Elimina el margen para evitar que exceda el padding */
  font-size: 50px;
}

.phrase {
  overflow-wrap: break-word; /* Permite que las palabras se dividan si son demasiado largas */
  word-wrap: break-word; /* Para compatibilidad con navegadores antiguos */
  width: 100%; /* Asegúrate de que el ancho sea 100% del contenedor */
  margin: 0; /* Elimina el margen para evitar que exceda el padding */
  font-style: italic;
}


.hero-image-main{
  width: 50%;
}

.image{
  width: 100%;
  height: 100%;
}

.hero-final{
  display: flex;
  padding: 3rem 2rem;
  justify-content: center;
}



.hero-image-final{
  width: 30%;
  align-items: center;
  justify-content: center;
  display: flex;
}

.callao-map {
  width: 65%;
  border-radius: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: transform 0.3s ease;
}

.callao-map:hover {
  transform: scale(1.05);
}

.hero-final-text{
  width: 50%;
  justify-content: center;
  display: flex;
  flex-direction: column;
}

.darkred-1{
  color: #4E171C;
  font-size: 35px;
}

.darkred-2{
  color: #4E171C;
  font-size: 25px;
}

@media only screen and (max-width: 900px){
  .hero-main{
    flex-direction: column;
  }

  .hero-final {
    flex-direction: column-reverse; /* Invertir el orden de los elementos */
    align-items: center; /* Centrar el contenido */
    gap: 1rem; /* Espacio entre el texto y la imagen */
  }

  .hero-title{
    width: 100%;
    padding: 3rem 1rem;
  }

  .hero-title h1{
    font-size: 30px;
    overflow-wrap: break-word;
  }

  .phrase{
    overflow-wrap: break-word;
  }

  .hero-image-main{
    width: 100%;
    object-fit: cover;
  }

  .hero-image-final{
    width: 100%;
  }

  .hero-final-text{
    width: 100%;
    text-align: center;
  }

  .darkred-1{
    font-size: 30px;
  }

  .darkred-2{
    font-size: 20px;
    padding-bottom: 1.5rem;
  }

  .callao-map{
    width: 45%;
  }
}

</style>