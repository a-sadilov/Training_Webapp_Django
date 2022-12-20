import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  /*{
    path: '/calendar',
    name: 'calendar',
    component: () => import(
      // webpackChunkName: "about" 
       '../views/Calendar.vue')
  },*/
  /*{
      path: '/training/:id',
    name: 'training-detail',
    component: () => import( '../views/TrainingDetail.vue')
  },*/
  {
      path: '/training-task/:id',
    name: 'training-task-detail',
    component: () => import( '../views/TrainingTaskDetail.vue')
  },
  /*{
      path: '/training-form',
    name: 'training-form',
    component: () => import('../views/TrainingForm.vue')
  },
  {
      path: '/training-task-form',
    name: 'training-task-form',
    component: () => import('../views/TrainingTaskForm.vue')
  },*/
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router