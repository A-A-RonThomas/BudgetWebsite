import { createRouter, createWebHistory } from 'vue-router';
import MainContent from '@/components/MainContent.vue';
import PurchaseList from '@/components/PurchaseList.vue';
import IncomeList from '@/components/IncomeList.vue';

// Define routes
const routes = [
  {
    path: '/',
    name: 'MainContent',
    component: MainContent, // Home component
  },

  {
    path: '/purchases',
    name: 'PurchaseList',
    component: PurchaseList,
  },

  {
    path: '/incomes',
    name: 'IncomeList',
    component: IncomeList,
  },
];

// Create and export the router instance
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL), // Use HTML5 history mode
  routes,
});

export default router;
