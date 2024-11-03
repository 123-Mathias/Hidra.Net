<script >

export default {
  name: "toolbar-content",
  components: {

  },
  data() {
    return {
      scrolled: false,
      menuOpen: false,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.scrolled = window.scrollY > 0;
    },
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
  },
};
</script>

<template>
  <div>
    <pv-toolbar :class="['toolbar-content', { 'scrolled-toolbar': scrolled }]">
      <template #start>
        <a href="#">
          <img src="/public/brand-logo/hidranet-brand.png" alt="Hidranet Logo"  class="brand">
        </a>
      </template>
      <template #center>

      </template>
      <template #end>
        <div v-if="!menuOpen" class="nav-links">
          <div v-if="!menuOpen" class="nav-links">
            <router-link to="/home" class="link-to">Inicio</router-link>
            <router-link to="/hidrants-net" class="link-to">Red de Hidrantes</router-link>
            <router-link to="/nearest-hidrant" class="link-to">Hidrantes cercanos</router-link>
          </div>
        </div>
        <div class="burger" @click="toggleMenu">
          <div :class="['line', { 'active': menuOpen }]"></div>
          <div :class="['line', { 'active': menuOpen }]"></div>
          <div :class="['line', { 'active': menuOpen }]"></div>
        </div>
      </template>
    </pv-toolbar>
    <div v-if="menuOpen" class="dropdown-menu">
      <router-link to="/home" class="dropdown-link" @click="toggleMenu">Inicio</router-link>
      <router-link to="/hidrants-net" class="dropdown-link" @click="toggleMenu">Red de Hidrantes</router-link>
      <router-link to="/nearest-hidrant" class="dropdown-link" @click="toggleMenu">Hidrantes cercanos</router-link>
    </div>
  </div>
</template>

<style scoped>

.brand{
  width: 200px;
  height: 40px;
  margin-top: 0.5rem;
}

.toolbar-content {
  background-color: #fff;
  padding: 1rem 2rem;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  transition: background-color 0.3s, box-shadow 0.3s;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #B3343E; /* Ajusta el grosor y color del borde */
  box-shadow: 0 2px 5px rgba(255, 0, 0, 0.34); /* Sombra que simula el "sombrado" */
}
h1 {
  color: #4E171C;
}

a{
  text-decoration: none;
  font-weight: bolder;
}

.link-to {
  color: #4E171C;
  margin-left: 1.5rem;
  margin-right: 1.5rem;
  font-size: 1.1rem;
  font-weight: 500;
  transition: all 0.3s;
}

.link-to:hover {
  color: #B3343E;
}


.burger {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 24px;
  height: 18px;
  cursor: pointer;
}

.line {
  width: 100%;
  height: 2px;
  background-color: #4E171C;
  transition: transform 0.3s, opacity 0.3s;
}

.line.active:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

.line.active:nth-child(2) {
  opacity: 0;
}

.line.active:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

.dropdown-menu {
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 75px;
  right: 0;
  left: 0;
  background-color: #fff;
  z-index: 999;
  padding: 2rem;
  box-shadow: 0 2px 5px rgba(255, 0, 0, 0.34); /* Sombra que simula el "sombrado" */
}

.dropdown-link {
  color: #4E171C;
  text-decoration: none;
  margin: 0.5rem 0;
  font-size: 1.1rem;
  font-weight: 500;
  transition: color 0.3s;
}

.dropdown-link:hover {
  color: #B3343E;
}

@media (max-width: 1050px) {
  .nav-links {
    display: none;
  }

  .burger {
    display: flex;
  }

  .nav-links.open {
    display: flex;
    flex-direction: column;
  }
}

</style>