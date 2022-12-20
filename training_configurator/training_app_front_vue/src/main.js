import { createApp } from 'vue'
import App from './App.vue'

import "vue-select/dist/vue-select.css";


import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import router from './router/index.js'
import HeaderNav from "@/components/HeaderNav"



import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const app = createApp(App)
app.component("HeaderNav", HeaderNav)

app.use(router).mount('#app')
