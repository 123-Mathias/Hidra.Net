<script >
export default {
  name: 'footer-content'
}
</script>

<template>

  <footer>
    <div class="info-section">
      <h1>Información</h1>
      <p>
        Contacto: 923 123 345
      </p>
      <p>
        Dirección: Los Helechos 123
      </p>
      <p>
        Correo: hidranet@hidra.net
      </p>
    </div>
    <div class="brand-section">
      <img src="/public/brand-logo/hidranet-brand-w.png" width="250">
      <hr class="separation">
      <div class="social-media-section">
        <div class="social-media-icon">
          <a href="https://x.com/" target="_blank">
            <img src="/public/social-media-icons/x-icon.png" alt="X icon" width="20">
          </a>
        </div>
        <div class="social-media-icon">
          <a href="https://www.instagram.com/" target="_blank">
            <img src="/public/social-media-icons/instagram-icon.png" alt="Instagram icon" width="25">
          </a>
        </div>
        <div class="social-media-icon">
          <a href="https://www.linkedin.com/feed/" target="_blank">
            <img src="/public/social-media-icons/linkedin-icon.png" alt="LinkedIn icon" width="25">
          </a>
        </div>
      </div>
    </div>
    <div class="info-section">
      <h1>Índice</h1>
      <div class="info-link">
        <img src="/public/social-media-icons/home-icon.png" alt="Home icon" width="20" height="20">
        <router-link to="/home" class="footer-links">Inicio</router-link>
      </div>
      <div class="info-link">
        <img src="/public/social-media-icons/hidrant-icon.png" alt="Home icon" width="20" height="20">
        <router-link to="/hidrants-net" class="footer-links">Red de Hidrantes</router-link>
      </div>
      <div class="info-link">
        <img src="/public/social-media-icons/location-icon.png" alt="Home icon" width="20" height="20">
        <router-link to="/nearest-hidrant" class="footer-links">Hidrantes cercanos</router-link>
      </div>
    </div>
  </footer>
  <div class="rights">
    <p>Todos los derechos reservados. © 2024. Hidra.Net</p>
  </div>
</template>

<style scoped>

.footer-links{
  text-decoration: none;
  padding-top: 0.25rem;
}

.separation{
  width: 70%;
  border-radius: 10px;
  margin: auto;
  border: #ffffff 1px solid;
  margin-bottom: 1.5rem;
}

footer {
  background-color: #4E171C;
  color: #fff;
  text-align: center;
  padding: 3.5rem 2rem;
  display: flex;
  justify-content: space-around;
}

.rights{
  background-color: #000;
  color: #fff;
  text-align: center;
  padding: 1.5rem 0rem 1.5rem 0rem;
}

.info-section{
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding-top: 1rem;
  text-align: left;
}

.info-link{
  display: flex;
  gap: 1rem;
  align-items: center;
}

.info-section h1{
  font-size: 1.2rem;
  color: #fff;
  padding-bottom: 0.4rem;
}

.social-media-section{
  display: flex;
  gap: 1.5rem;
  justify-content: center;
}

.social-media-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #fff;
  transition: 0.43s;
}

.social-media-icon:hover{
  box-shadow: 0px 0px 13px 0px #fff;
}

.social-media-icon img {
  vertical-align: middle;
}

@media screen and (max-width: 850px) {
  footer {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .social-media-section {
    padding-top: 1rem;
  }

  .brand-section {
    order: 3; /* Mueve esta sección al final */
  }

  .info-section {
    order: 1; /* Mantiene las secciones de información al principio */
  }

  .info-section:nth-of-type(2) {
    order: 2; /* Asegura que el segundo info-section esté en el medio */
  }

  .social-media-section {
    padding-top: 2rem;
  }
}

</style>