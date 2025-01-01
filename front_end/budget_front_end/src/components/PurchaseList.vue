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
              <td class="table-style">${{ purchase.amount }}</td>
              <td class="table-style">{{ titlize(purchase.account) }}</td>
              <td>
                <input
                  type="text"
                  v-model="purchase.budget_category"
                  placeholder="Budget Category"
                  class="form-input formatted-input"
                  />
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
    }
  },

  computed: {
    ...mapGetters(["activeDate"]),
  },
  
  watch: {
    activeDate(newDate) {
      if (newDate){
          this.fetchPurchases(); // Fetch budgets for the new activeDate
      }
    },
  },

  methods: {
    async fetchPurchases() {
        if (!this.activeDate) {
            console.warn("activeDate is not available yet.");
            return;
        }
        try {
            console.log(this.activeDate);
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


},

created() {
    this.fetchPurchases();
}

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
