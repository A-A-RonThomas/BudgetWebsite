<template>
  <div>
    <!-- <button @click="saveBudgets" class="save-btn">Save Budget</button> -->
    
    <BudgetCategoryTable
      title="Fixed Expenses"
      :Categories="categories.fixed"
      @add-row="addRow('fixed', $event)"
      @delete-row="deleteRow('fixed', $event)"
      @modified="markModified"
    />

    <hr />

    <BudgetCategoryTable
      title="Variable Expenses"
      :Categories="categories.variable"
      @add-row="addRow('variable', $event)"
      @delete-row="deleteRow('variable', $event)"
      @modified="markModified"
    />

    <hr />

    <SinkingFundTable
      title="Sinking Funds"
      :Categories="categories.sinkingFunds"
      @add-row="addRow('sinkingFunds', $event)"
      @delete-row="deleteRow('sinkingFunds', $event)"
      @modified="markModified"
    />

  </div>
</template>

<script>
import axios from "axios";
import BudgetCategoryTable from "./BudgetCategoryTable.vue";
import SinkingFundTable from "./SinkingFundTable.vue";
import { mapGetters } from "vuex";
import saveOnExitMixin from "@/mixins/saveOnExitMixin";

export default {
  name: "MainContent",
  components: {
    BudgetCategoryTable,
    SinkingFundTable,
  },

  mixins: [saveOnExitMixin],

  beforeRouteLeave(to, from, next) {
    saveOnExitMixin.beforeRouteLeave.call(this, to, from, () => {
      next();
    })
  },

  computed: {
    ...mapGetters(["activeDate"]),
  },

  data() {
    return {
      categories: {
        fixed: [],
        variable: [],
        sinkingFunds: [],
      },
      currentDate: "",
      isModified: false,
    };
  },

  watch: {
    activeDate(newDate) {
      this.currentDate = newDate; // Update currentDate when activeDate changes
      this.fetchBudgets(); // Fetch budgets for the new activeDate
    },
  },


  methods: {
    hasUnsavedChanges() {
      return this.isModified; // Check if data has been modified
    },

    markModified() {
      this.isModified = true; // Mark data as modified
    },

    async saveBudgets() {
      const budgetData = {
        date: this.currentDate,
        budgets: this.categories,
      };

      try {
        await axios.post(
          "http://localhost:8000/save-budget",
          budgetData
        );

      } catch (error) {
        console.error("Error saving budgets:", error);
        alert("Failed to save budgets.");
      }
    },

    async fetchBudgets() {
      try {
        const response = await axios.get(
          `http://localhost:8000/get-budget-${this.currentDate}`
        );
        const { fixed, variable, sinkingFunds } = response.data.message;

        this.categories.fixed = fixed || [];
        this.categories.variable = variable || [];
        this.categories.sinkingFunds = sinkingFunds || [];
      } catch (error) {
        console.error("Error fetching budgets:", error);
        alert("Failed to fetch budgets.");
      }
    },

    addRow(type, newCategory) {
      this.categories[type].push(newCategory);
    },

    deleteRow(type, index) {
      this.categories[type].splice(index, 1);
    },
  },

  created() {
    this.currentDate = this.activeDate;
    this.fetchBudgets();
    // console.log("From mainContent:", this.currentDate);
  },
};
</script>
