import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    redirect: "Home",
  },
  {
    path: "/Home",
    name: "Home",
    component: () => import("../components/Home/Home.vue"),
  },
  {
    path: "/Auth",
    name: "Auth",
    component: () => import("../components/Auth/Auth.vue"),
  },
  {
    path: "/Relation",
    name: "Relation",
    component: () => import("../components/Relation/Relation.vue"),
  },
  {
    path: "/Search",
    name: "Search",
    component: () => import("../components/Search/Search.vue"),
  },
  {
    path: "/Profile",
    name: "Profile",
    component: () => import("../components/Profile/Profile.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
