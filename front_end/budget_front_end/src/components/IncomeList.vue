<template>
    <div class="container mt-4">
      <h2>Incomes</h2>
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
          <tr v-for="income in incomes" :key="income.id">
              <td>{{ income.date }}</td>
              <td>{{ income.description }}</td>
              <td>${{ income.amount }}</td>
              <td>{{ titlize(income.account) }}</td>
              <td>{{ income.budget_category }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>

<script>
import axios from 'axios';
import { mapGetters } from "vuex";


export default {
  name: 'IncomeList',
  props: {

  },

  data() {
    return {
        incomes: {},
    }
  },

  computed: {
    ...mapGetters(["activeDate"]),
  },
  
  watch: {
    activeDate(newDate) {
      if (newDate){
          this.fetchIncomes(); // Fetch budgets for the new activeDate
      }
    },
  },

  methods: {
    async fetchIncomes() {
        if (!this.activeDate) {
            console.warn("activeDate is not available yet.");
            return;
        }
        try {
            console.log(this.activeDate);
            const response = await axios.get(
            `http://localhost:8000/transaction/get_all_incomes/${this.activeDate}`
            );

            this.incomes = response.data.incomes;

            console.log(this.incomes);
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
    this.fetchIncomes();
}

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
