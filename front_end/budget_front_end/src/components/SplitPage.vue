<template>
<div class="split-page">
  <div class="left-panel">
    <BudgetView ref="budgetView" />
  </div>
  <div class="right-panel">
    <PurchaseList @update-purchases="updateBudgetActual" ref="purchaseListView" />
  </div>
</div>
</template>

<script>
import BudgetView from "@/components/BudgetView.vue";
import PurchaseList from "@/components/PurchaseList.vue";

export default {
  name: "SplitPage",
  components: {
    BudgetView,
    PurchaseList,
  },  
  beforeRouteLeave(to, from, next) {
    const budgetView = this.$refs.budgetView;
    const purchaseListView = this.$refs.purchaseListView;

    // Create an array of promises for saving data
    const savePromises = [];

    if (budgetView && budgetView.hasUnsavedChanges()) {
      savePromises.push(budgetView.saveBudgets());
    }

    if (purchaseListView && purchaseListView.hasUnsavedChanges()) {
      savePromises.push(purchaseListView.saveBudgets());
    }

    // Handle all save operations before navigation
    Promise.allSettled(savePromises).then((results) => {
      // Log errors if any save operation fails
      results.forEach((result) => {
        if (result.status === "rejected") {
          console.error("Error during save operation:", result.reason);
        }
      });

      // Allow navigation regardless of save operation success
      next();
    });
  },


  methods: {
    updateBudgetActual(categoryName, amount) {
      const budgetView = this.$refs.budgetView;
      if (budgetView) {
        budgetView.updateBudgetActual(categoryName, amount);
      } else {
        console.error('budgetView is not defined');
      }
    },

  },
};


</script>


<style scoped>
.split-page {
  display: flex;
  height: 100vh; 
  overflow: hidden; 
}

.left-panel,
.right-panel {
  flex: 1;
  overflow-y: auto; 
  border: 1px solid #ddd;
}

.left-panel {
  background-color: #f9f9f9;
}

.right-panel {
  background-color: #ffffff;
}
.left-panel::-webkit-scrollbar,
.right-panel::-webkit-scrollbar {
width: 6px; 
}

.left-panel::-webkit-scrollbar-track,
.right-panel::-webkit-scrollbar-track {
background: #f1f1f1; 
}

.left-panel::-webkit-scrollbar-thumb,
.right-panel::-webkit-scrollbar-thumb {
background: #888; 
border-radius: 10px; 
}

.left-panel::-webkit-scrollbar-thumb:hover,
.right-panel::-webkit-scrollbar-thumb:hover {
background: #555; 
}

</style>
  