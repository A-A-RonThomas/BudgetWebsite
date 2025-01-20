<template>
    <div class="container mt-4">
      <h2>Purchases</h2>
      <table class="table table-striped table-bordered">
        <thead class="thead-dark">
          <tr>
              <th>Date</th>
              <th>Description</th>
              <th>Amount</th>
              <th>Account</th>
              <th>Budget Category</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="purchase in purchases" :key="purchase.id">
              <td class="table-style">{{ purchase.date }}</td>
              <td class="table-style">{{ purchase.description }}</td>
              <td class="table-style">${{ purchase.amount * -1 }}</td>
              <td class="table-style">{{ titlize(purchase.account) }}</td>
              <td>
                <select
                  v-model="purchase.budget_category"
                  class="form-select formatted-input"
                  @change="handleBudgetCategoryChange(purchase)"
                >
                  <option v-for="item in budgetItems" :key="item" :value="item">
                    {{ item }}
                  </option>
                </select>
              </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>

<script>
import axios from 'axios';
import { mapGetters } from "vuex";
import saveOnExitMixin from '@/mixins/saveOnExitMixin';


export default {
  name: 'PurchaseList',
  mixins : [saveOnExitMixin],
  props: {

  },

  data() {
    return {
        purchases: {},
        isModified: false
    }
  },

  computed: {
    ...mapGetters(["budgetItems", "activeDate"]),
  },
  
  watch: {
    activeDate(newDate) {
      if (newDate){
          this.fetchPurchases(); // Fetch budgets for the new activeDate
      }
    },
  },

  beforeRouteLeave(to, from, next) {
    saveOnExitMixin.beforeRouteLeave.call(this, to, from, () => {
      next();
    })
  },

  methods: {
    handleBudgetCategoryChange(purchase) {
      this.isModified = true;
      this.$emit('update-purchases', purchase);
    },
    hasUnsavedChanges() {
      return this.isModified; // Check if data has been modified
    },
    async fetchPurchases() {
        if (!this.activeDate) {
            console.warn("activeDate is not available yet.");
            return;
        }
        try {
            const response = await axios.get(
            `http://localhost:8000/transaction/get_all_purchases/${this.activeDate}`
            );

            this.purchases = response.data.purchases;


        } catch (error) {
            console.error("Error fetching purchases:", error);
            alert("Failed to fetch purchases.");
        }
    },

    titlize(text) {
        return text.replace(/\b\w/g, (char) => char.toUpperCase());
    },
    async saveBudgets(){
      this.isModified = false;
      console.log("Hit SaveBudgets in purchaseList View");
    }


},

created() {
    this.fetchPurchases();
}

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
