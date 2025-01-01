// src/store/index.js
import { createStore } from "vuex";

const store = createStore({
  state: {
    currentDate: new Date().toISOString().slice(0, 7),
    activeDate: new Date().toISOString().slice(0, 7), // Default value in "YYYY-MM" format
  },

  mutations: {
    setCurrentDate(state, newDate) {
      state.currentDate = newDate.toISOString().slice(0, 7); // Update currentDate
    },

    setActiveDate(state, newDate) {
      state.activeDate = newDate.toISOString().slice(0, 7); // Update activeDate
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
  },

  getters: {
    currentDate(state) {
      return state.currentDate;
    },

    activeDate(state) {
      return state.activeDate;
    },
  },
});

export default store;
