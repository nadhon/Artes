import { createRouter, createWebHistory } from 'vue-router'
import Home from '../view/Home.vue'
import Sobre from '../view/Sobre.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sobre',
    name: 'Sobre',
    component: Sobre
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
