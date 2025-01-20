// src/store/index.js
import { createStore } from "vuex";

const store = createStore({
  state: {
    currentDate: new Date().toISOString().slice(0, 7),
    activeDate: new Date().toISOString().slice(0, 7), // Default value in "YYYY-MM" format
    budgetItems: [],
  },

  mutations: {
    setCurrentDate(state, newDate) {
      state.currentDate = newDate.toISOString().slice(0, 7); // Update currentDate
    },

    setActiveDate(state, newDate) {
      state.activeDate = newDate.toISOString().slice(0, 7); // Update activeDate
    },

    setBudgetItems(state, items) {
      state.budgetItems = items;
    },

    addBudgetItem(state, item) {
      state.budgetItems.push(item);
    },

    removeBudgetItem(state, item) {
      state.budgetItems = state.budgetItems.filter((i) => i !== item);
    },
  },

  actions: {
    updateCurrentDate({ commit }, newDate) {
      commit("setCurrentDate", newDate); // Call mutation to update state
    },

    updateActiveDate({ commit }, newDate) {
      if (newDate instanceof Date) {
        commit("setActiveDate", newDate); // Update activeDate
        // console.log(`UpdateActiveDate hit with ${newDate}`);
      } else {
        console.error("Invalid Date supplied to updateActiveDate");
      }
    },

    updateBudgetItems({ commit }, items) {
      commit('setBudgetItems', items);
    },

    addBudgetItem({ commit }, item) {
      commit('addBudgetItem', item);
    },

    removeBudgetItem({ commit }, item) {
      commit('removeBudgetItem', item);
    },
  },

  getters: {
    currentDate(state) {
      return state.currentDate;
    },

    activeDate(state) {
      return state.activeDate;
    },

    budgetItems: (state) => state.budgetItems,
  },
});

export default store;
