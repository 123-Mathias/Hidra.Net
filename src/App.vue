<script>
import {defineComponent} from "vue";
import FooterContent from "./public/components/footer-content.component.vue";
import ToolbarContent from "./public/components/toolbar-content.component.vue";

export default defineComponent({
  components: {ToolbarContent, FooterContent}
})
</script>

<template>
  <toolbar-content>
  </toolbar-content>
  <br>
  <br>
  <router-view></router-view>
  <footer-content>
  </footer-content>
</template>

<style scoped>

</style>
