<template>
  <div class="budget-category-table">
    <h2 class="table-title">
      <input
        type="text"
        :value="title"
        placeholder="Title"
        class="form-input formatted-input"
        @blur="$emit('update:title', $event.target.value)"
      />
    </h2>
    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Expected</th>
          <th>Actual</th>
          <!-- <th>Difference</th> -->
          <!-- <th>Actions</th> -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in Categories" :key="index" 
            :class="{'bg-light-red': item.ending_value < 0, 'hovered': hoveredRow === index}"
            @mouseenter="hoveredRow = index" 
            @mouseleave="hoveredRow = null">
          <td>
            <input
              type="text"
              v-model="item.name"
              placeholder="Name"
              class="form-input formatted-input"
              @input="notifyModified"
            />
          </td>
          <td>
            <input
              type="number"
              v-model.number="item.expected"
              placeholder="Expected"
              class="form-input formatted-input"
              @input="notifyModified"
            />
          </td>
          <td>
            <span class="formatted-value">
              {{ Math.round(item.actual * 100) / 100 }}
            </span>
          </td>
          <td class="no-background">
                <button 
                  v-show="hoveredRow === index" 
                  @click="deleteRow(index)" 
                  class="btn btn-danger rounded-circle p-0 delete-btn"
                >
                X
                </button>
          </td>
        </tr>
      </tbody>
    </table>
    <button @click="addRow" class="add-row-btn">New Row</button>
  </div>
</template>

<script>
export default {
  name: "BudgetCategoryTable",
  props: {
    title: {
      type: String,
      required: true,
    },
    Categories: {
      type: Array,
      required: true,
    },
  },
  computed: {
 
  },
  data() {
    return {
      hoveredRow: null, // Track hovered row
    };
  },
  methods: {
    addRow() {
      const newCategory = {
        name: "",
        expected: 0,
        actual: 0,
      };
      this.$emit("add-row", newCategory); // Notify parent to add a row
      this.notifyModified(); // Notify parent of modification
    },
    deleteRow(index) {
      const confirmed = window.confirm("Are you sure you want to delete this item? This cannot be undone.");
      if (confirmed) {
        this.$emit("delete-row", index); // Notify parent to delete a row
        this.notifyModified(); // Notify parent of modification
      }
    },
    notifyModified() {
      this.$emit("modified"); // Notify parent of data modification
    },
    updateTitle(newTitle) {
      this.$emit("update:title", newTitle); // Emit updated title to parent
      this.notifyModified(); // Notify parent of modification
    },
    calculateEndingValue(startingValue, added) {
      return Math.round((startingValue - added) * 100) / 100;
    },
  },
};
</script>


<style scoped>
.no-background{
  background-color: transparent !important; /* Removes background */
  border: none !important; /* Removes table cell borders */
}

</style>
