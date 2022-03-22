import { createRouter, createWebHashHistory } from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import pageNum1 from '../views/pageNum1.vue'
import pageNum2 from '../views/pageNum2.vue'

const routes = [
    {
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld
    },
    {
        path: '/pageNum1',
        name: 'pageNum1',
        component: pageNum1
    },
    {
        path: '/pageNum2',
        name: 'pageNum2',
        component: pageNum2
    },
    {
        path: '',
        redirect: '/pageNum1'
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
