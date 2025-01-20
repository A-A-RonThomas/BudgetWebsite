import { createRouter, createWebHistory } from 'vue-router';
import SplitPage from '@/components/SplitPage.vue';
import PurchaseList from '@/components/PurchaseList.vue';
import IncomeList from '@/components/IncomeList.vue';

// Define routes
const routes = [
  {
    path: '/',
    name: 'SplitPage',
    component: SplitPage,
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
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
