<template>
    <div class="top-bar">
      <button @click="changeMonth(-1)" class="arrow-btn">&larr;</button>
      <div class="month-year">{{ currentMonthYear }}</div>
      <button @click="changeMonth(1)" class="arrow-btn">&rarr;</button>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from "vuex";
  
  export default {
    name: "TopNavigation",
    computed: {
      currentMonthYear() {
      // Ensure activeDate is a Date object
      const date = typeof this.activeDate === "string"
        ? new Date(`${this.activeDate}-15`)
        : this.activeDate;

      // Format to "Month Year" (e.g., "January 2025")
      return date.toLocaleString("default", {
        month: "long",
        year: "numeric",
      });
    },
      ...mapGetters(["currentDate", "activeDate"]),
    },
    methods: {
      ...mapActions(["updateActiveDate", "updateCurrentDate"]),
      changeMonth(direction) {
        const newDate = new Date(this.activeDate + "-10");
        newDate.setMonth(newDate.getMonth() + direction);
        this.updateActiveDate(newDate);
      },
    },
  };
  </script>
  
  <style scoped>
  .top-bar {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .month-year {
    font-size: 1.2rem;
    font-weight: bold;
    margin: 0 20px;
  }
  
  .arrow-btn {
    background: none;
    border: none;
    color: black;
    font-size: 1.5rem;
    cursor: pointer;
    padding: 5px 10px;
  }
  
  .arrow-btn:hover {
    color: #007bff;
  }
  </style>
  