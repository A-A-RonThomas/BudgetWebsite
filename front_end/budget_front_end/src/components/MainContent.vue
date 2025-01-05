<template>
  <div>
    
    <div v-for="(non_fundItems, non_fundKey) in non_funds" :key="non_fundKey">
      <BudgetCategoryTable
        :title="non_fundKey"
        :Categories="non_fundItems"
        @update:title="updateNonFundKey(non_fundKey, $event)"
        @add-row="addRow(non_fundKey, $event)"
        @delete-row="deleteRow(non_fundKey, $event)"
        @modified="markModified"
      />
      <hr />
    </div>
    <div v-for="(fundItems, fundKey) in funds" :key="fundKey">
      <SinkingFundTable
        :title="formatTitle(fundKey)"
        :Categories="fundItems"
        @add-row="addFundRow(fundKey, $event)"
        @delete-row="deleteFundRow(fundKey, $event)"
        @modified="markModified"
      />
      <hr v-if="Object.keys(funds).length > 1" />
    </div>

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
      non_funds: {

      },
      funds: {

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
    updateNonFundKey(oldKey, newKey) {
      if (oldKey !== newKey && newKey.trim() !== "") {
        // Add the new key with the same data
        this.non_funds[newKey] = this.non_funds[oldKey];

        // Delete the old key
        delete this.non_funds[oldKey];

        this.markModified(); // Notify changes
      }
    },
    formatTitle(key) {
      // Convert camelCase to Title Case (e.g., sinkingFunds -> Sinking Funds)
      return key.replace(/([A-Z])/g, " $1").replace(/^./, (str) => str.toUpperCase());
    },
    hasUnsavedChanges() {
      return this.isModified; // Check if data has been modified
    },

    markModified() {
      this.isModified = true; // Mark data as modified
    },

    async saveBudgets() {
      const budgetData = {
        date: this.currentDate,
        budget_tables: {'non_funds': this.non_funds, 'funds': this.funds},
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
      this.non_funds = {};
      this.funds = {};
      try {
        const response = await axios.get(
          `http://localhost:8000/get-budget-${this.currentDate}`
        );
        var response_data = response.data.message.budget;
        
        for (const key in response_data.non_fund) {
          this.non_funds[key] = response_data.non_fund[key]
        }

        for (const key in response_data.fund) {
          this.funds[key] = response_data.fund[key]
        }
      } catch (error) {
        console.error("Error fetching budgets:", error);
        alert("Failed to fetch budgets.");
      }
    },

    async deleteBudgetItem(budgetItem, isFund) {
      const info = {
        item: budgetItem,
        type: isFund
      }
      try {
        await axios.post(
          "http://127.0.0.1:8000/delete-budget-item",
          info
        )
      }
      catch (error) {
        console.error("Error deleting budget item:", error);
        alert("Failed to delete budget item.");
      }
    },

    addRow(type, newCategory) {
      this.non_funds[type].push(newCategory);
    },

    addFundRow(type, newCategory) {
      this.funds[type].push(newCategory);
    },

    deleteRow(type, index) {
      this.deleteBudgetItem(this.non_funds[type][index], 0)
      this.non_funds[type].splice(index, 1);
    },

    deleteFundRow(type, index) {
      this.funds[type].splice(index,1);
    }
  },

  created() {
    this.currentDate = this.activeDate;
    this.fetchBudgets();
    // console.log("From mainContent:", this.currentDate);
  },
};
</script>
