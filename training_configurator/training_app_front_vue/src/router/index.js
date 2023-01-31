import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  /*{
    path: '/calendar',
    name: 'calendar',
    component: () => import(
      // webpackChunkName: "about" 
       '../views/Calendar.vue')
  },*/
  {
    path: '/dashboard',
    name: 'dashboard-view',
    component: () => import( '../views/DashboardView.vue')
  },
  {
    path: '/event/:id',
    name: 'event-detail',
    component: () => import( '../views/EventDetail.vue')
  },
  {
      path: '/task/:id',
    name: 'task-detail',
    component: () => import( '../views/TaskDetail.vue')
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