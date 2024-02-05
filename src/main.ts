import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
// import 'sweetalert2/dist/sweetalert2.css'

createApp(App).use(router).mount('#app')
