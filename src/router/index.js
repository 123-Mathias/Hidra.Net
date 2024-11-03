import {createRouter, createWebHistory} from "vue-router";

import HeroContentComponent from "../hero/hero-content.component.vue";
import HidrantsNetContentComponent from "../hidrants-net/hidrants-net-content.component.vue";
import NearestHidrantContentComponent from "../nearest-hidrant/nearest-hidrant-content.component.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/home', component: HeroContentComponent, meta: { title: 'Home' } },
        { path: '/hidrants-net', component: HidrantsNetContentComponent, meta: { title: 'Hidrants Net' } },
        { path: '/nearest-hidrant', component: NearestHidrantContentComponent, meta: { title: 'Nearest Hidrant' } },
        { path: '/', redirect: '/home' },
    ],
});

export default router;