<template>
  <button @click="addTable('non_fund')">Add Budget Table</button>
  <button @click="addTable('fund')">Add Sinking Fund Table</button>
  <div>
    
    <div v-for="(table,key) in non_funds" :key="key">
      <BudgetCategoryTable
        :title="table.name"
        :Categories="table.items"
        @update:title="updateNonFundTableName(key, $event)"
        @add-row="addRow(key, $event)"
        @delete-row="deleteRow(key, $event)"
        @modified="markModified"
      />
      <hr />
    </div>
    <div v-for="(table, key) in funds" :key="key">
      <SinkingFundTable
        :title="table.name"
        :Categories="table.items"
        @update:title="updateFundTableName(key, $event)"
        @add-row="addFundRow(key, $event)"
        @delete-row="deleteFundRow(key, $event)"
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
  name: "BudgetView",
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
      mapped_purchases: [],
      currentDate: "",
      isModified: false,
    };
  },

  watch: {
    activeDate(newDate) {
      if (this.isModified){
        this.saveBudgets();
      }
      this.currentDate = newDate;
      this.fetchBudgets();
      this.isModified = false;
    },
  },


  methods: {
    updateBudgetActual(purchase) {

      // Step 1: Check if the purchase already exists in mapped_purchases
      const existingPurchase = this.mapped_purchases.find((item) => item.id === purchase.id);

      if (existingPurchase) {
        // Update the budget_category and amount of the existing purchase
        existingPurchase.budget_category = purchase.budget_category;
        existingPurchase.amount = purchase.amount;
      } else {
        // Add the new purchase to mapped_purchases
        this.mapped_purchases.push(purchase);
      }

      // Step 2: Reset all actual/minus fields in non_funds and funds
      const resetFields = (tables, field) => {
        for (const key in tables) {
          tables[key].items.forEach((item) => {
            item[field] = 0;
          });
        }
      };

      resetFields(this.non_funds, "actual");
      resetFields(this.funds, "minus");

      // Step 3: Resum all purchases and update the actual/minus fields
      const updateFields = (tables, field, purchases) => {
        purchases.forEach((purchase) => {
          for (const key in tables) {
            const table = tables[key];
            const category = table.items.find((item) => item.name === purchase.budget_category);
            if (category) {
              category[field] += (purchase.amount * -1); // Accumulate the total amount
            }
          }
        });
      };

      updateFields(this.non_funds, "actual", this.mapped_purchases);
      updateFields(this.funds, "minus", this.mapped_purchases);

      // Step 4: Mark as modified and sync budget items
      this.markModified();
      this.syncBudgetItems();
    },




    syncBudgetItems() {
      const allItems = [
        ...Object.values(this.non_funds).flatMap((table) => table.items.map((item) => item.name)),
        ...Object.values(this.funds).flatMap((table) => table.items.map((item) => item.name)),
      ];
      this.$store.dispatch('updateBudgetItems', allItems);
    },

    addTable(tableType) {
      if (tableType === "non_fund") {
        this.non_funds[new Date().toISOString()] = {
          items: [{ name: "New Budget Item", actual: 0 }],
          name: "New Budget Table",
        };
      } else {
        this.funds[new Date().toISOString()] = {
          items: [{ name: "New Fund Item", actual: 0 }],
          name: "New Fund Table",
        };
      }
    },

    updateFundTableName(key, newName) {
      this.funds[key]['name'] = newName;
      this.markModified(); // Notify changes
    },
    updateNonFundTableName(key, newName) {
      this.non_funds[key]['name'] = newName;
      this.markModified(); // Notify changes
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
      console.log("SaveBudgets called");
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
      this.non_funds[type].items.push(newCategory);
      this.syncBudgetItems();
    },

    addFundRow(type, newCategory) {
      this.funds[type].items.push(newCategory);
      this.syncBudgetItems();
    },

    deleteRow(type, index) {
      this.deleteBudgetItem(this.non_funds[type].items[index], 0)
      this.non_funds[type].items.splice(index, 1);
      this.syncBudgetItems();
    },

    deleteFundRow(type, index) {
      this.funds[type].items.splice(index,1);
      this.syncBudgetItems();
    }
  },

  created() {
    this.currentDate = this.activeDate;
    this.fetchBudgets().then(() => this.syncBudgetItems());
    // console.log("From mainContent:", this.currentDate);
  },
};
</script>
