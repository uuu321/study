import { createApp } from 'vue'
import App from './App.vue'

// createApp(App).mount('#app')
import router from './router/index'
const app = createApp(App)
app.use(router)
//app.use(router) 需放在app.mount('#app')前面
app.mount('#app')
