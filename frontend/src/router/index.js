import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import('../components/home.vue')
  },
  {
    path: "/",
    name: "team",
    component: () => import('../components/Team.vue')
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
