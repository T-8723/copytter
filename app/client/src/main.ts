import { createApp } from "vue";
import App from "./App/App.vue";
import router from "./views/router";
import axios from "axios";
import store from "./common/store";
import VueAxios from "vue-axios";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

const app = createApp(App);

app.use(router).use(store).use(ElementPlus).use(VueAxios, axios).mount("#app");
